from django.core.urlresolvers import reverse
from django.test import TestCase
from shortener.models import Link


class ViewsTest(TestCase):

    def test_create_link(self):
        response = self.client.get(reverse("links:create"))
        url = "http://google.com/"

        response = self.client.post(reverse("links:create"),
            {"url": url}, follow=True)

        assert response.status_code == 200

        self.assertIn(url, response.content)

    def test_create_short_link(self):
        url = 'https://alexanderae.com'

        response = self.client.post(reverse("links:create"),
            {"url": url}, follow=True)

        link = Link.objects.get(url=url)

        self.assertIn(link.short_url, response.content)
