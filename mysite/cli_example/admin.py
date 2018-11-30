from django.contrib import admin
from .models import Country, Island, Region, Province, City, Baranggay, Resident
# Register your models here.

admin.site.site_header = 'Project Pirena'

class CountryAdmin(admin.ModelAdmin):
	list_display = ('name', 'date_created')
	list_filter = ('name', 'date_created')
admin.site.register(Country, CountryAdmin)

class IslandAdmin(admin.ModelAdmin):
	list_display = ('name', 'region', 'date_created')
	list_filter = ('region', 'date_created')
	search_fields = ('island', 'region')
admin.site.register(Island, IslandAdmin)

class RegionAdmin(admin.ModelAdmin):
	list_display = ('name', 'province', 'date_created')
	list_filter = ('province', 'date_created')
	search_fields = ('region', 'province')
admin.site.register(Region, RegionAdmin)

class ProvinceAdmin(admin.ModelAdmin):
	list_display = ('name', 'city', 'date_created')
	list_filter = ('city', 'date_created')
	search_fields = ('province', 'city')
admin.site.register(Province, ProvinceAdmin)

class BaranggayAdmin(admin.ModelAdmin):
	list_display = ('name', 'date_created')
	list_filter = ('name', 'date_created')
	search_fields = ('name', 'date_created')
admin.site.register(Baranggay, BaranggayAdmin)


class CityAdmin(admin.ModelAdmin):
	list_display = ('name', 'baranggay', 'date_created')
	list_filter = ('baranggay', 'date_created')
	search_fields = ('city', 'baranggay')
admin.site.register(City, CityAdmin)


class ResidentAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'baranggay', 'date_created')
	list_filter = ('country', 'date_created')
	search_fields = ('first_name', 'last_name')
admin.site.register(Resident, ResidentAdmin)
