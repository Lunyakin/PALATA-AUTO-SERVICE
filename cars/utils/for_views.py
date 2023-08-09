import datetime
import time

from django.shortcuts import get_object_or_404
from transliterate import slugify

from cars.models import CarPhoto
from cars.models.car import Car
from cars.models.car_note import CarNote, CarNotePhoto


def create_slug(
        car_brand: str = None,
        car_model: str = None,
        reg_number: str = None) -> str:
    text = f'{car_brand} {car_model} {reg_number}ы'
    text = slugify(text).rstrip('y')
    return text


def delete_car(slug: str) -> object:
    """Удаление машины (перевод в состояние НЕ АКТИВНЫЙ)"""
    data = Car.objects.get(slug=slug)
    data.is_deleted = True
    data.save()
    return data


def save_car(clean_data: dict, user: object, file=None):
    car = Car(
        user=user,
        car_brand=clean_data['car_brand'],
        car_model=clean_data['car_brand'],
        release_year=clean_data['release_year'],
        reg_number=clean_data['reg_number'],
        vin_code=clean_data['vin_code'],
        mileage=clean_data['mileage'],
        slug=create_slug(
            car_brand=clean_data['car_brand'],
            car_model=clean_data['car_brand'],
            reg_number=clean_data['reg_number']
        )
    )
    car.save()
    if file:
        car_photo = CarPhoto(
            photo=file,
            car=car
        )
        car_photo.save()


def save_note_about_car(clean_data: dict, car: object, list_of_photos: list, *args):
    add = str(datetime.datetime.now().microsecond)
    temp = f"{clean_data['title']} {add}ыы"
    note_slug = slugify(temp).rstrip('yy')

    note = CarNote(title=clean_data['title'], text=clean_data['text'], slug=note_slug, car=car, )
    note.save()
    if list_of_photos:
        for _ in list_of_photos:
            photo_for_note = CarNotePhoto(photo=_, car_note=note, *args)
            photo_for_note.save()


def update_note(clean_data, list_of_photos, note_slug):
    note = get_object_or_404(CarNote.objects.filter(slug=note_slug))
    note.title = clean_data['title']
    note.text = clean_data['text']
    note.save()
    if list_of_photos:
        for _ in list_of_photos:
            photo_for_note = CarNotePhoto(photo=_, car_note=note)
            photo_for_note.save()
    car = get_object_or_404(Car.objects.filter(car_note__slug=note_slug))
    return car.slug
