from share_count.services.base import Service

__all__ = ['twitter',]

class TwitterService(Service):
    service_url = "http://urls.api.twitter.com/1/urls/count.json"
    url_param = 'url'
    doctype = 'json'
    selector = "count"

twitter = TwitterService()
