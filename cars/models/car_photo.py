from django.db import models
from django.shortcuts import reverse

from cars.models import Car
from cars.utils.for_models import path_for_cars_foto


class CarPhoto(models.Model):
    photo = models.ImageField(
        upload_to=path_for_cars_foto, null=True, verbose_name='Фотография'
    )
    created_data = models.DateField(auto_now_add=True)

    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='car_photo')

    class Mate:
        verbose_name = 'Фотография машины'
        verbose_name_plural = 'Фотографии машины'
