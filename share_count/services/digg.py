from share_count.services.base import Service

__all__ = ['digg',]

class DiggService(Service):
    service_url = "http://services.digg.com/2.0/story.getInfo"
    url_param = 'links'
    doctype = 'json'
    
    # NOTE: URLs for Digg need to be normalized

    def selector(self, content):
        stories = content['stories'] or [{'diggs': 0}]
        return sum(story['diggs'] for story in stories)

digg = DiggService()
