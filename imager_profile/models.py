from __future__ import unicode_literals
from django.db import models
import uuid
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
from django.db.models.signals import post_save
from django.dispatch import receiver

import logging
logr = logging.getLogger(__name__)


@receiver(post_save, sender=User)
def make_sure_user_profile_is_added_on_user_created(sender, **kwargs):
    """Receives a signal from user creation and makes a profile."""
    if kwargs.get('created', False):
        Photographer.objects.create(user=kwargs.get('instance'))


@python_2_unicode_compatible
class PhotographerProfileManager(models.Manager):
    '''returns a queryset pre-filtered to only active profiles'''
    class Meta:
        model = "Photographer"

    def get_queryset(self):
        return User.objects.filter(is_active=True)


@python_2_unicode_compatible
class Photographer(models.Model):
    """Photographer fulfills the 'user profile' role for us"""
    user_uuid = models.UUIDField(primary_key=True,
                                 default=uuid.uuid4,
                                 editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name="photographer")
    has_portfolios = models.BooleanField(default=False)
    portfolio_url = models.CharField(max_length=255, blank=True)

    def __str__(self):
        fn = self.user.get_full_name().strip() or self.user.get_username()
        return "{}: {}".format(fn, self.user_uuid)

    @property
    def is_active(self):
        return self.user.is_active

    objects = models.Manager()
    active = PhotographerProfileManager()


@python_2_unicode_compatible
class Address(models.Model):
    photographer = models.ForeignKey(
        Photographer,
        on_delete=models.CASCADE,
        related_name="address",)
    default = models.BooleanField('Default Address', default=False)
    address_1 = models.CharField('Street Address 1',
                                 max_length=255,
                                 blank=True,
                                 default='',)
    address_2 = models.CharField('Street Address 2',
                                 max_length=255,
                                 blank=True,
                                 default='',)
    city = models.CharField('City',
                            max_length=128,
                            blank=True,
                            default='',)
    state = models.CharField('State',
                             max_length=2,
                             blank=True,
                             default='',)
    post_code = models.CharField('Zip Code',
                                 max_length=7,
                                 blank=True,
                                 default='',)
