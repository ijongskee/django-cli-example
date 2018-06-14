from django.contrib import admin
from .models import City, Baranggay, Residence
# Register your models here.

admin.site.register(City)
admin.site.register(Baranggay)
admin.site.register(Residence)

