from django.contrib import admin

from cars.models.car import Car


class CarsAdmin(admin.ModelAdmin):
    list_display = ('car_brand', 'car_model', 'release_year', 'reg_number', 'vin_code', 'user', 'is_deleted')
    list_display_links = ('car_brand', 'car_model', 'release_year', 'reg_number', 'vin_code', 'user')
    search_fields = ('reg_number', 'vin_code',)
    prepopulated_fields = {'slug': ('car_brand', 'car_model', 'reg_number')}


admin.site.register(Car, CarsAdmin)
