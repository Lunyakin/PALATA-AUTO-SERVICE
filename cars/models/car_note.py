from django.db import models
from django.urls import reverse

from cars.models.car import Car
from cars.utils.for_models import path_for_note_foto


class CarNote(models.Model):
    title = models.CharField(max_length=50, blank=False, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Описание')
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=50, unique=True, db_index=True)

    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='car_note')

    class Mate:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'
        ordering = ('-update_date',)

    def __str__(self):
        return f'{self.pk} {self.title}'

    def get_absolute_url(self):
        return reverse('cars:detail-note', kwargs={'car_note': self.slug})


class CarNotePhoto(models.Model):
    photo = models.ImageField(upload_to=path_for_note_foto, null=True)
    created_date = models.DateField(auto_now_add=True)

    car_note = models.ForeignKey(CarNote, on_delete=models.CASCADE, to_field='id', related_name='car_note_photo')

    class Mate:
        verbose_name = 'Фотография к заметке'
        verbose_name_plural = 'Фотографии к заметке'

    def get_absolute_url(self):
        return reverse('car_note_foto', kwargs={'car_note_foto': self.pk})

    def delete(self, using=None, keep_parents=False):
        self.photo.delete()
        super().delete()

