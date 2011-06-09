from share_count.services.base import Service

__all__ = ['reddit',]

class RedditService(Service):
    service_url = "http://www.reddit.com/api/info.json"
    url_param = 'url'
    doctype = 'json'

    # NOTE: URLs for Reddit need to be normalized

    def selector(self, content):
        data = content['data'] or {'children': []}
        return sum((child['data'] or {'score': 0})['score'] for child in \
                   data['children'])

reddit = RedditService()
