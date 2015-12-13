# -*- coding: utf-8 -*-

from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse
from .utils import encode_to_alphabet


class Link(models.Model):
    url = models.URLField('Enlace original', unique=True, db_index=True)
    slug = models.CharField('Fragmento de URL corta', max_length=10, blank=True)

    class Meta:
        verbose_name = "Link"
        verbose_name_plural = "Links"

    def __unicode__(self):
        return self.url

    def get_absolute_url(self):
        return reverse('links:update', kwargs={'pk': self.id})

    def save(self, *args, **kwargs):
        super(Link, self).save(*args, **kwargs)

        if not self.slug:
            self.encode_url()
            super(Link, self).save(*args, **kwargs)

    def encode_url(self):
        """
        Crea el slug para la url original
        """
        self.slug = encode_to_alphabet(self.id)

    @property
    def short_url(self):
        """
        Retorna la url en versión corta
        """
        return settings.SITE_URL + self.slug
