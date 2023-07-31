from django.db import models
from django.shortcuts import reverse

from cars.utils.for_models import path_for_cars_foto


class Car(models.Model):
    user = models.ForeignKey(
        to='users.User', related_name='car', on_delete=models.PROTECT
    )
    car_brand = models.CharField(
        max_length=20, unique=False, blank=False, null=False, verbose_name='Марка машины'
    )
    car_model = models.CharField(
        max_length=20, unique=False, blank=False, null=False, verbose_name='Модель машины'
    )
    release_year = models.CharField(
        max_length=4, unique=False, blank=False, null=False, verbose_name='Год выпуска'
    )
    reg_number = models.CharField(
        max_length=10, unique=True, blank=False, null=False, verbose_name='Регистрационный номер'
    )
    vin_code = models.CharField(
        max_length=17, unique=True, blank=False, null=False, verbose_name='ВинКод'
    )
    mileage = models.PositiveIntegerField(
        null=False, blank=False, verbose_name='Километраж'
    )
    created_date = models.DateField(auto_now_add=True)
    is_deleted = models.BooleanField(verbose_name='Удалена', default=False)
    slug = models.SlugField(
        max_length=50, unique=True,
        db_index=True,
    )

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'

    def __str__(self):
        return self.reg_number

    def get_absolute_url(self):
        return reverse('cars:detail-car-info', kwargs={'car': self.slug})
