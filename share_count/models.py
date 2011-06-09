from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from share_count import services

ENABLED_SERVICES = getattr(settings, 'ENABLED_SERVICES', ['twitter'])

class Counts(models.Model):
    url = models.URLField(
        verify_exists=getattr(settings, 'SHARE_COUNT_VERIFY_URLS', True),
        max_length=getattr(setting, 'SHARE_COUNT_URL_LENGTH', 500)
    )

    content_type = models.ForeignKey(ContentType, null=True)
    object_id = models.PositiveIntegerField(null=True)
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    digg = models.PositiveIntegerField(default=0)
    facebook = models.PositiveIntegerField(default=0)
    googlebuzz = models.PositiveIntegerField(default=0)
    linkedin = models.PositiveIntegerField(default=0)
    reddit = models.PositiveIntegerField(default=0)
    stumbleupon = models.PositiveIntegerField(default=0)
    twitter = models.PositiveIntegerField(default=0)

    @property
    def total(self):
        return sum([self.digg, self.facebook, self.googlebuzz, self.linkedin, self.reddit, self.stumbleupon, self.twitter])

    def update_counts(self, commit=True):
        for service in ENABLED_SERVICES:
            count = getattr(services, service).get_count(self.url)
            setattr(self, service, count)
        if commit:
            self.save()
