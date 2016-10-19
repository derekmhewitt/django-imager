from __future__ import unicode_literals
import factory
from django.contrib.auth.models import User


class UserFactory(factory.django.DjangoModelFactory):
    """creates fake users for testing purposes"""
    class Meta:
        model = User

    username = factory.Sequence(lambda n: "user{}".format(n))
    email = factory.Sequence(lambda n: "user{}@somedomain.com")
