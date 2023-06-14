from transliterate import slugify

from cars.models import Cars


def create_slug(
        car_brand: str = None,
        car_model: str = None,
        reg_number: str = None) -> str:
    text = f'{car_brand} {car_model} {reg_number}ы'
    text = slugify(text).rstrip('y')
    return text


def delete_car(slug: str) -> object:
    """Удаление машины (перевод в состояние НЕ АКТИВНЫЙ)"""
    data = Cars.objects.get(slug=slug)
    data.is_deleted = True
    data.save()
    return data
