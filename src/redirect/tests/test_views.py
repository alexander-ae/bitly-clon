from django.test import TestCase
from shortener.models import Link


class ViewsTest(TestCase):

    def test_redirect(self):
        url = "http://google.com/"

        link = Link(url=url)
        link.save()

        response = self.client.get(link.short_url, follow=True)

        assert response.redirect_chain[1][0] == link.url
