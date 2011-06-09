import json
import re
import requests

from pyquery import PyQuery
from lxml import etree

__all__ = ['Service']

class Service(object):
    service_url = None
    url_param = 'url'
    doctype = 'json'
    selector = 'count'
    jsonp_callback = None

    def get_count(self, url):
        raw_response = self.get_response(url)
        if self.doctype == 'json':
            content = raw_response.content
            if self.jsonp_callback:
                regex = r"%s\((.*)\)(\s*?;\s*?)?$" % \
                        re.escape(self.jsonp_callback)
                jsonp = re.compile(regex, re.MULTILINE)
                m = jsonp.match(content)
                content = m.group(1)
            response = json.loads(content)
        elif self.doctype == 'xml':
            response = etree.fromstring(raw_response.content)
        else:
            response = raw_response
        return self.handle_response(response)

    def get_response(self, url, **params):
        params[self.url_param] = url
        return requests.get(self.service_url, params=params)

    def handle_response(self, response):
        if callable(self.selector):
            return self.prepare_response(self.selector(response))
        elif self.doctype == 'xml':
            node = PyQuery(response)(self.selector)
            return self.prepare_response(node.text())
        elif self.doctype == 'json' or (hasattr(response, '__getitem__') and \
                                        not isinstance(response, basestring)):
            y = response
            for x in self.selector.split('.'):
                y = y[x]
            return self.prepare_response(y)
        else:
            return self.prepare_response(response)

    def prepare_response(self, value):
        if isinstance(value, basestring):
            value = value.lower()
            if value.endswith("k"):
                return int(value[:-1]) * 1000
            elif value.endswith("m"):
                return int(value[:-1] * 1000000)
        return int(value)
