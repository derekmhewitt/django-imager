from __future__ import unicode_literals
from django.test import TestCase, override_settings
from django.test.client import Client
from django.urls import reverse
from django.contrib.auth.models import User
from imager_images.models import Photo, Album
from .factory import PhotoFactory, AlbumFactory
from imager_profile.tests.factory import UserFactory
import datetime
import tempfile
from taggit.models import Tag

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
        """verify that new photos are saved correctly"""
        self.assertEqual(len(self.user.photos.all()), 0)
        self.photo = PhotoFactory(user=self.user)
        self.assertEqual(len(self.user.photos.all()), 1)

    def test_multiple_photos_created(self):
        """verify that multiple new photos are saved correctly"""
        self.assertEqual(len(self.user.photos.all()), 0)
        self.photo = PhotoFactory(user=self.user)
        self.photo = PhotoFactory(user=self.user)
        self.photo = PhotoFactory(user=self.user)
        self.photo = PhotoFactory(user=self.user)
        self.assertEqual(len(self.user.photos.all()), 4)

    def test_photo_creation_modified_dates(self):
        """verify that created and modified dates updated correctly"""
        self.photo = PhotoFactory(user=self.user)
        self.assertEqual(self.photo.date_created, self.today)
        self.assertEqual(self.photo.date_modified, self.today)

    def test_photo_title(self):
        """verify photo titles are saved correctly"""
        self.photo = PhotoFactory(user=self.user)
        self.assertTrue(isinstance(self.photo.description, str))


@override_settings(MEDIA_ROOT=TEST_MEDIA_ROOT)
class AlbumTestCase(TestCase):
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
        """verify album creation works properly"""
        self.album = AlbumFactory(user=self.user)
        self.assertTrue(isinstance(self.album, Album))

    def test_new_album_has_no_photos(self):
        """verify new album has no photos after creation"""
        self.album = AlbumFactory(user=self.user)
        self.assertEqual(len(self.album.photos.all()), 0)

    def test_album_has_5_photos(self):
        """verify album has 5 photos after making 5"""
        self.album = AlbumFactory(user=self.user)
        self.album.photos.add(*PhotoFactory.create_batch(5,
                              user=self.user))
        self.assertEqual(len(self.album.photos.all()), 5)

    def test_album_creation_modified_dates(self):
        """verify album creation and modified dates work as expected"""
        self.album = AlbumFactory(user=self.user)
        self.assertEqual(self.album.date_created, self.today)
        self.assertEqual(self.album.date_modified, self.today)


class LibraryViewTestCase(TestCase):
    """Test the library view"""

    def setUp(self):
        """Set up a fake things for testing."""
        self.user = User(username='test_user')
        self.user.set_password('test_password')
        self.user.save()
        self.c = Client()
        self.c.force_login(user=self.user)
        self.today = datetime.date.today()
        self.album = AlbumFactory(user=self.user)
        self.album.photos.add(*PhotoFactory.create_batch(7,
                              user=self.user))

    def tearDown(self):
        """Tear down setUp'd things"""
        del self.album
        del self.user
        del self.c

    def test_pagination_library_page_one(self):
        """test pagination on the first photo library page"""
        response = self.c.get(reverse('my_library'))
        self.assertEqual(len(response.context['all_photos']), 4)

    def test_pagination_library_page_two(self):
        """test pagination on the second photo library page"""
        response = self.c.get('/images/?page_photo=2')
        self.assertEqual(len(response.context['all_photos']), 3)

    def test_pagination_library_redirect(self):
        """test that pagination out of range redirects to the
        last page for photos"""
        response = self.c.get('/images/?page_photo=3')
        self.assertEqual(len(response.context['all_photos']), 3)

    def test_pagination_album_page_one(self):
        """test pagination on the first album library page"""
        self.albums = AlbumFactory.create_batch(6, user=self.user)
        response = self.c.get(reverse('my_library'))
        self.assertEqual(len(response.context['all_albums']), 4)

    def test_pagination_album_page_two(self):
        """test pagination on the second album library page"""
        self.albums = AlbumFactory.create_batch(6, user=self.user)
        response = self.c.get('/images/?page_album=2')
        self.assertEqual(len(response.context['all_albums']), 3)

    def test_pagination_album_redirect(self):
        """test that pagination out of range redirects to the
        last page for albums"""
        self.albums = AlbumFactory.create_batch(6, user=self.user)
        response = self.c.get('/images/?page_album=3')
        self.assertEqual(len(response.context['all_albums']), 3)

    def test_pagination_album_photo_pages(self):
        """test that moving album pages leaves photo page alone"""
        self.albums = AlbumFactory.create_batch(5, user=self.user)
        response = self.c.get('/images/?page_album=2')
        self.assertIn(b"?page_album=1&page_photo=1", response.content)

    def test_pagination_photo_album_pages(self):
        """test that moving photo pages leaves album page alone"""
        self.albums = AlbumFactory.create_batch(5, user=self.user)
        response = self.c.get('/images/?page_photo=2')
        self.assertIn(b"?page_photo=1&page_album=1", response.content)


class AlbumViewTestCase(TestCase):
    """verify that the album view behaves as we expect"""

    def setUp(self):
        """Set up a fake things for testing."""
        self.user = User(username='test_user')
        self.user.set_password('test_password')
        self.user.save()
        self.c = Client()
        self.c.force_login(user=self.user)
        self.today = datetime.date.today()
        self.album = AlbumFactory(user=self.user)
        self.album.photos.add(*PhotoFactory.create_batch(7,
                              user=self.user))

    def tearDown(self):
        """Tear down setUp'd things"""
        del self.album
        del self.user
        del self.c

    def test_pagination_album_view_page_one(self):
        """test pagination on the single album page"""
        response = self.c.get('/images/album/{}/'.format(self.album.pk))
        self.assertEqual(len(response.context['album_photos']), 4)

    def test_pagination_album_view_page_two(self):
        """test pagination on the single album page two"""
        response = self.c.get('/images/album/{}/?page_photo=2'.format(self.album.pk))
        self.assertEqual(len(response.context['album_photos']), 3)

    def test_pagination_album_view_redirect(self):
        """test that pagination out of range redirects to the
        last page for album photos"""
        response = self.c.get('/images/album/{}/?page_photo=3'.format(self.album.pk))
        self.assertEqual(len(response.context['album_photos']), 3)


class TagViewTestCase(TestCase):
    """verify that the tag view does what we expect"""

    def setUp(self):
        """Set up a fake things for testing."""
        self.user = User(username='test_user')
        self.user.set_password('test_password')
        self.user.save()
        self.c = Client()
        self.c.force_login(user=self.user)
        self.today = datetime.date.today()
        self.album = AlbumFactory(user=self.user)

    def tearDown(self):
        """Tear down setUp'd things"""
        del self.album
        del self.user
        del self.c
        del self.photo

    def test_tags_are_in_response_library_view(self):
        """verify that tags are returned to the library view"""
        self.photo = PhotoFactory(user=self.user)
        self.photo.tags.add("Zebra")
        response = self.c.get(reverse('my_library'))
        self.assertIn(b"Zebra", response.content)

    def test_tags_are_in_response_tag_view(self):
        """verify that tags are returned to the tag view"""
        self.photo = PhotoFactory(user=self.user)
        self.photo.tags.add("Burrito")
        response = self.c.get(reverse('tag_view', kwargs={'tag': "Burrito"}))
        self.assertIn(b"Burrito", response.content)

    def test_tags_are_in_response_photo_view(self):
        """verify that tags are returned to the photo view"""
        self.photo = PhotoFactory(user=self.user)
        self.photo.tags.add("Taco")
        response = self.c.get(reverse('photo_view', args=[self.photo.pk]))
        self.assertIn(b"Taco", response.content)

    def test_multiple_tags_assign_correctly(self):
        """verify that multiple tags assign and can be queried properly"""
        self.photo = PhotoFactory(user=self.user)
        self.photo.tags.add("Taco")
        self.photo.tags.add("Burrito")
        self.photo.tags.add("Zebra")
        self.assertEqual(len(self.photo.tags.all()), 3)
