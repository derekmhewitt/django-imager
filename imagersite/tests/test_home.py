from django.test import TestCase
from django.urls import reverse

class TestHomePage(TestCase):
    """Contains test methods for our home page."""

    def setUp(self):
        self.response = self.client.get("/")

    def tearDown(self):
        pass

    def test_home_page_exists(self):
        self.assertEquals(self.response.status_code, 200)

    def test_home_page_uses_correct_templates(self):
        templates = ['imagersite/layout.html', 'imagersite/home.html']
        for template in templates:
            self.assertTemplateUsed(self.response, template)

    def test_home_page_has_login_link(self):
        expected = reverse("auth_login")
        self.assertContains(self.response, expected)
