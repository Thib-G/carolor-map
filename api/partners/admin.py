from django.contrib.gis import admin
from .models import Category, Partner

# Register your models here.
admin.site.register(Partner, admin.OSMGeoAdmin)
admin.site.register(Category)