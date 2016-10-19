from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from imager_profile.models import PhotographerProfileManager
from imager_profile.models import Photographer, Address


class TestPhotographerProfileModel(TestCase):
    """Create test class for patron profile manager model."""

    def setUp(self):
        """Set up a fake user for testing."""
        self.user = User(username='test_user')
        self.user.set_password('test_password')
        self.user.save()

    def tearDown(self):
        """Tear down setUp'd things"""
        del self.user

    def test_user_exists(self):
        """Test that the setup user we made exists."""
        self.assertTrue(self.user is not None)

    def test_username_is_correct(self):
        """Test that the fake user's username set correctly."""
        self.assertEqual(self.user.username, 'test_user')

    def test_user_photographer_exists(self):
        """Test that creating the user creates a photographer along with it."""
        self.assertTrue(self.user.photographer is not None)

    def test_photographer_attached_to_this_user(self):
        """Test that the user's photographer we created is attached to the
        test user."""
        self.assertEqual(self.user.photographer.user.username, 'test_user')


class TestPhotographerModel(TestCase):
    """Create test class for photographer model."""

    def setUp(self):
        """set up fake stuff for testing"""
        self.user = User(username='test_user')
        self.user.set_password('test_password')
        self.user.save()

    def tearDown(self):
        """tear down fake testing stuff"""
        del self.user

    def test_photographer_dunder_str(self):
        """test that __str__ on photographer returns full name or username."""
        self.assertTrue(str(self.user.photographer), 'test_user')

    def test_photographer_is_active_property(self):
        """test photographer is active property works"""
        self.assertTrue(self.user.photographer.is_active)

    def test_photographer_is_active_property_inactive_user(self):
        """test photographer is active property doesn't work with inactive
        user"""
        self.user.is_active = False
        self.assertFalse(self.user.photographer.is_active)


class TestAddressModel(TestCase):
    """Create test class for address model."""

    def setUp(self):
        """set up fake stuff for testing"""
        self.user = User(username='test_user')
        self.user.set_password('test_password')
        self.user.save()
        address = Address(photographer=self.user.photographer, default=True,
                          address_1="1234 Baker Way", address_2="Appt #7",
                          city="Seattle", state="WA", post_code="98101")
        address.save()

    def tearDown(self):
        """tear down fake testing stuff"""
        del self.user

    def test_address_model_creation(self):
        """verify that address models are created properly"""
        address = Address(photographer=self.user.photographer, default=False,
                          address_1="4321 Walker Way", address_2="Appt #5",
                          city="Tacoma", state="OR", post_code="98102")
        address.save()
        self.assertTrue(len(self.user.photographer.address.all()), 2)

    def test_address_model_fields(self):
        """verify data in address model fields is recorded properly"""
        address = self.user.photographer.address.filter(default=True).first()
        self.assertTrue(address.address_1, "1234 Baker Way")

    def test_address_model_belongs_to_user(self):
        """verify that model belongs to correct user"""
        address = self.user.photographer.address.filter(default=True).first()
        self.assertEqual(address.photographer, self.user.photographer)


class TestPhotographerProfileManager(TestCase):
    """Create a test class for photographer profile manager"""

    def setUp(self):
        """set up fake stuff for testing"""
        self.user = User(username='test_user')
        self.user.set_password('test_password')
        self.user.save()

    def tearDown(self):
        """tear down fake testing stuff"""
        del self.user

    def test_profile_manager_returns_only_active_users(self):
        self.user = User(username="inactive_user")
        self.user.is_active = False
        self.user.save()
        query = PhotographerProfileManager.get_queryset(self)
        self.assertTrue(len(query), 1)
