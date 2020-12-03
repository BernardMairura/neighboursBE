from django.contrib import admin
from django.contrib import admin
from .models import Neighborhood,ResidentProfile,Business,HoodadminProfile

# Register your models here.
admin.site.register(Neighborhood)
admin.site.register(ResidentProfile)
admin.site.register(Business)
admin.site.register(HoodadminProfile)


