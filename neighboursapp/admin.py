from django.contrib import admin
from django.contrib import admin
from .models import Neighborhood,NeighborProfile,Business,HoodadminProfile

# Register your models here.
admin.site.register(Neighborhood)
admin.site.register(NeighborProfile)
admin.site.register(Business)
admin.site.register(HoodadminProfile)


