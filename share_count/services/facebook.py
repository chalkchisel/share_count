from django.conf import settings
from share_count.services.base import Service

__all__ = ['facebook',]

# Possible Facebook parameters: 'share_count', 'like_count', 'comment_count', 
#                               'total_count' and 'commentsbox_count'

class FacebookService(Service):
    service_url = "https://api.facebook.com/method/fql.query"
    url_param = 'query'
    doctype = 'xml'
    fb_param = getattr(settings, 'SHARE_COUNT_FACEBOOK_ATTRIBUTE', 'total_count')
    selector = lambda self, x: x[0][0].text

    def get_response(self, url, **params):
        query = 'SELECT %s FROM link_stat WHERE url="%s"' % (self.fb_param,
                url.replace('"', '\"'))
        return super(FacebookService, self).get_response(query, **params)

facebook = FacebookService()
