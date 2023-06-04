from django.db import models
from django.shortcuts import reverse

from cars.utils.for_models import path_for_cars_foto


class Cars(models.Model):
    user = models.ForeignKey(
        to='users.User', related_name='car', on_delete=models.PROTECT
    )
    car_brand = models.CharField(
        max_length=20, unique=False, blank=False, null=False
    )
    car_model = models.CharField(
        max_length=20, unique=False, blank=False, null=False
    )
    release_year = models.CharField(
        max_length=4, unique=False, blank=False, null=False
    )
    reg_number = models.CharField(
        max_length=10, unique=True, blank=False, null=False
    )
    vin_code = models.CharField(
        max_length=17, unique=True, blank=False, null=False
    )
    mileage = models.PositiveIntegerField(
        null=False, blank=False
    )
    car_photo = models.ImageField(
        upload_to=path_for_cars_foto,
        blank=True, null=True
    )
    created_date = models.DateField(auto_now_add=True)
    slug = models.SlugField(
        max_length=50, unique=True,
        db_index=True,
    )

    def __str__(self):
        return self.reg_number

    def get_absolute_url(self):
        return reverse('car', kwargs={'car': self.slug})
