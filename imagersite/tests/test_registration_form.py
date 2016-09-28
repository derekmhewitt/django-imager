from django.test import TestCase
from django.urls import reverse


class TestRegistrationForm(TestCase):
    """Contains test methods for our registration form page."""

    def setUp(self):
        self.response = self.client.get("/")

    def tearDown(self):
        pass

    def test_activate(self):
        pass
