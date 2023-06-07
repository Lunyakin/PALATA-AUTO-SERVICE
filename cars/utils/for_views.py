from transliterate import slugify


def create_slug(
        car_brand: str = None,
        car_model: str = None,
        reg_number: str = None) -> str:
    text = f'{car_brand} {car_model} {reg_number}ы'
    text = slugify(text).rstrip('y')
    return text
