from django.db import models


class Page(models.Model):

    title = models.CharField(
        max_length=256
    )

    slug = models.SlugField()

    parent = models.ForeignKey(
        "self",
        blank=True,
        null=True
    )

    site = models.ForeignKey(
        'sites.Site'
    )

    order = models.PositiveIntegerField(
        default=0
    )

    def __unicode__(self):
        return self.title

    class Meta:
        unique_together = ('slug', 'parent', 'site')
