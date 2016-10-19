from __future__ import unicode_literals
from django.test import TestCase, override_settings
from django.contrib.auth.models import User
from imager_images.models import Photo, Album
from .factory import PhotoFactory, AlbumFactory
from imager_profile.tests.factory import UserFactory
import datetime
import tempfile

TEST_MEDIA_ROOT = tempfile.mkdtemp()


@override_settings(MEDIA_ROOT=TEST_MEDIA_ROOT)
class PhotoTestCase(TestCase):
    """create test class for photo model"""

    def setUp(self):
        """Set up a fake user for testing."""
        self.user = User(username='test_user')
        self.user.set_password('test_password')
        self.user.save()
        self.client.force_login(user=self.user)
        self.today = datetime.date.today()

    def tearDown(self):
        """Tear down setUp'd things"""
        del self.user
        del self.client

    def test_photo_creation(self):
        self.assertEqual(len(self.user.photos.all()), 0)
        self.photo = PhotoFactory(user=self.user)
        self.assertEqual(len(self.user.photos.all()), 1)

    def test_multiple_photos_created(self):
        self.assertEqual(len(self.user.photos.all()), 0)
        self.photo = PhotoFactory(user=self.user)
        self.photo = PhotoFactory(user=self.user)
        self.photo = PhotoFactory(user=self.user)
        self.photo = PhotoFactory(user=self.user)
        self.assertEqual(len(self.user.photos.all()), 4)

    def test_photo_creation_modified_dates(self):
        self.photo = PhotoFactory(user=self.user)
        self.assertEqual(self.photo.date_created, self.today)
        self.assertEqual(self.photo.date_modified, self.today)

    def test_photo_title(self):
        self.photo = PhotoFactory(user=self.user)
        self.assertTrue(isinstance(self.photo.description, str))


@override_settings(MEDIA_ROOT=TEST_MEDIA_ROOT)
class AlbumTestCast(TestCase):
    """create test class for album model"""

    def setUp(self):
        """Set up a fake user for testing."""
        self.user = User(username='test_user')
        self.user.set_password('test_password')
        self.user.save()
        self.client.force_login(user=self.user)
        self.today = datetime.date.today()

    def tearDown(self):
        """Tear down setUp'd things"""
        del self.user
        del self.client

    def test_album_created(self):
        self.album = AlbumFactory(user=self.user)
        self.assertTrue(isinstance(self.album, Album))

    def test_new_album_has_no_photos(self):
        self.album = AlbumFactory(user=self.user)
        self.assertEqual(len(self.album.photos.all()), 0)

    def test_album_has_5_photos(self):
        self.album = AlbumFactory(user=self.user)
        self.album.photos.add(*PhotoFactory.create_batch(5,
                              user=self.user))
        self.assertEqual(len(self.album.photos.all()), 5)

    def test_album_creation_modified_dates(self):
        self.album = AlbumFactory(user=self.user)
        self.assertEqual(self.album.date_created, self.today)
        self.assertEqual(self.album.date_modified, self.today)
"""
OK, so I had a conversation with Cris about testing.  First of all, I'm going to go after our models with a buzzsaw and cut out just about everything that isn't explicitely required as part of the assignment.  Additional things to do:
- create factory.py in each tests directory, our factories live there
- remember the difference between PhotoFactory.create() and .build() <-- this lets us test that properties instantiate properly when we save things manually inside our tests.
- Test created-on and last-modified dates by comparison - modify an extra property on the instance of the model and assert those dates are different, and that modified is after created.
- create a different test_modelname file for each model and another diff test file for every other major division."""
