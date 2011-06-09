from share_count.services.base import Service

__all__ = ['linkedin',]

class LinkedInService(Service):
    service_url = "http://www.linkedin.com/cws/share-count"
    url_param = 'url'
    doctype = 'json'
    selector = "count"
    jsonp_callback = "IN.Tags.Share.handleCount"

linkedin = LinkedInService()
