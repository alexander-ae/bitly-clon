from django.db import models


class Link(models.Model):
    url = models.URLField('Enlace original', unique=True)

    class Meta:
        verbose_name = "Link"
        verbose_name_plural = "Links"

    def __unicode__(self):
        return self.url

    @property
    def short_url(self):
        pass
