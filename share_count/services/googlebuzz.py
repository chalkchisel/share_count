from share_count.services.base import Service

__all__ = ['googlebuzz',]

class GoogleBuzzService(Service):
    service_url = "http://www.linkedin.com/cws/share-count"
    url_param = 'url'
    doctype = 'json'
    selector = "count"
    jsonp_callback = "google_buzz_set_count"

googlebuzz = GoogleBuzzService()
