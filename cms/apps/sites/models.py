from django.db import models


class Site(models.Model):

    name = models.CharField(
        max_length=2048,
        help_text="Friendly name for the site"
    )

    domain = models.CharField(
        max_length=2048,
        help_text="Domain name for the site. Example: 'example.com'"
    )

    def __unicode__(self):
        return self.name
