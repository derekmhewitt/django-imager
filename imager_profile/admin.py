from django.contrib import admin
from imager_profile.models import (Photographer, Address,
                                   Equipment, SocialMedia)

# Register your models here.
admin.site.register(Photographer)
admin.site.register(Address)
admin.site.register(Equipment)
admin.site.register(SocialMedia)
