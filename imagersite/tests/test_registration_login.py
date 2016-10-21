from django.test import TestCase


class TestRegistrationLogin(TestCase):
    """Contains test methods for our login page."""

    def setUp(self):
        self.response = self.client.get("/accounts/login/")

    def tearDown(self):
        pass

    def test_login_page_exists(self):
        self.assertEquals(self.response.status_code, 200)

    def test_login_page_uses_correct_template(self):
        self.assertTemplateUsed(self.response, "registration/login.html")

    def test_login_page_uses_layout_template(self):
        self.assertTemplateUsed(self.response, "imagersite/layout.html")

    def test_login_form_username_field(self):
        self.assertIn(b'name="username"', self.response.content)

    def test_login_form_password_field(self):
        self.assertIn(b'name="password"', self.response.content)

    def test_login_form_submit_button(self):
        self.assertIn(b'value="login"', self.response.content)
