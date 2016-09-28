from django.test import TestCase
from django.urls import reverse


class TestHomePage(TestCase):
    """Contains test methods for our home page."""

    def setUp(self):
        self.response = self.client.get("/")

    def tearDown(self):
        pass

    def test_activate(self):
        # expected = reverse('registration_activation_complete')
        pass
