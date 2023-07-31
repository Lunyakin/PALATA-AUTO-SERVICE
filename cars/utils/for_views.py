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


def save_note_about_car_without_photos(clean_data: dict, car: object):
    note = CarNote(title=clean_data['title'], descriptions=clean_data['descriptions'], car=car)
    note.save()


def save_note_about_car_with_photos(clean_data: dict, car: object, list_of_photos: list, *args):
    note = CarNote(title=clean_data['title'], descriptions=clean_data['descriptions'], car=car)
    note.save()
    for _ in list_of_photos:
        photo_for_note = CarNotePhoto(photo=_, car_note=note, *args)
        photo_for_note.save()
