from __future__ import unicode_literals
import factory
from faker import Factory as FakerFactory
from imager_images.models import Photo, Album
from imager_profile.tests.factory import UserFactory

fake = FakerFactory.create()

# remember the difference between PhotoFactory.create() and .build() <--
# this lets us test that properties instantiate properly when we save
# things manually inside our tests.


class PhotoFactory(factory.django.DjangoModelFactory):
    """creates fake photo models for testing purposes"""
    class Meta:
        model = Photo

    user = factory.SubFactory(UserFactory)
    file = factory.django.ImageField(color="blue")
    title = factory.lazy_attribute(lambda n: fake.sentence(nb_words=5))


class AlbumFactory(factory.django.DjangoModelFactory):
    """creates fake albums for testing purposes"""
    class Meta:
        model = Album

    user = factory.SubFactory(UserFactory)
    title = factory.lazy_attribute(lambda n: fake.sentence(nb_words=4))
    description = factory.lazy_attribute(lambda n: fake.sentence(nb_words=3))
    cover_photo = factory.django.ImageField(color="yellow")
