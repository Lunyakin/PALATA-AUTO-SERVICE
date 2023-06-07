from django.contrib import admin

from cars.models import Cars


class CarsAdmin(admin.ModelAdmin):
    list_display = ('car_brand', 'car_model', 'release_year', 'reg_number', 'vin_code', 'user')
    list_display_links = ('car_brand', 'car_model', 'release_year', 'reg_number', 'vin_code', 'user')
    search_fields = ('reg_number', 'vin_code',)
    prepopulated_fields = {'slug': ('car_brand', 'car_model', 'reg_number')}


admin.site.register(Cars, CarsAdmin)
