from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible
from datetime import datetime


def user_directory_path(instance, filename):
    ''' file will be uploaded to MEDIA_ROOT/user_<id>/%Y%m%d<filename>
        this is not true it will return: MEDIA_ROOT/user_<id>/<filename>
    '''
    now = datetime.now()
    return 'user_{0}/{2}/{1}'.format(
        instance.user.id, filename, now.strftime('%Y%m%d'))


@python_2_unicode_compatible
class Photo(models.Model):
    '''A Photo belonging to a usr'''
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    albums = models.ManyToManyField('Album', blank=True)
    file = models.ImageField(upload_to=user_directory_path,
                             height_field=None,
                             width_field=None, max_length=100)
    title = models.CharField("Title", max_length=255, blank=True)
    height_field = models.IntegerField("Height", blank=True)
    width_field = models.IntegerField("Width", blank=True)
    latitude = models.IntegerField("Latitude", blank=True)
    longitude = models.IntegerField("Longitude", blank=True)
    camera = models.CharField("Camera", max_length=64, blank=True)
    lens = models.CharField("Lens", max_length=64, blank=True)
    focal_length = models.CharField("Focal Length", max_length=32, blank=True)
    shutter_speed = models.IntegerField("Shutter Speed", blank=True)
    aperture = models.CharField("Aperture", max_length=64, blank=True)
    description = models.CharField("Description", max_length=255, blank=True)
    date_created = models.DateField('Date Created', auto_now_add=True)
    date_modified = models.DateField('Date Modified', auto_now=True)
    published = models.CharField(max_length=64,
                                 choices=[('private', 'private'),
                                          ('shared', 'shared'),
                                          ('public', 'public')])
    is_public = models.BooleanField('Is_public?', default=False)

    def __str__(self):
        '''Method returns a string we can use to ID this model instance.'''
        return str(self.file)

    class Meta:
        ordering = ('date_created',)


@python_2_unicode_compatible
class Album(models.Model):
    '''An Album of Photos'''
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    title = models.CharField("Title", max_length=255, blank=True)
    description = models.CharField("Description", max_length=255, blank=True)
    cover_photo = models.CharField("Cover Photo", max_length=255, blank=True)
    date_created = models.DateField('Date Created', auto_now_add=True)
    date_modified = models.DateField('Date Modified', auto_now=True)
    published = models.CharField(max_length=64,
                                 choices=[('private', 'private'),
                                          ('shared', 'shared'),
                                          ('public', 'public')])

    def __str__(self):
        return self.title
