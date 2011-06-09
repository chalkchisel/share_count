from django.conf import settings
from share_count.services.base import Service

__all__ = ['stumbleupon',]

class StumbleUponService(Service):
    service_url = "http://www.stumbleupon.com/badge/embed/5/"
    url_param = 'url'
    doctype = 'xml'
    selector = ".count"

stumbleupon = StumbleUponService()
