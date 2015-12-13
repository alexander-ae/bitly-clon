from django.core.urlresolvers import reverse
from django.test import TestCase


class ViewsTest(TestCase):
    def test_create_link(self):
        response = self.client.get(reverse("links:create"))
        url = "http://google.com/"

        response = self.client.post(reverse("links:create"),
            {"url": url}, follow=True)

        assert response.status_code == 200

        self.assertIn("google.com", response.content)
