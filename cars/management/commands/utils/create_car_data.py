from django.contrib.auth import get_user_model

from cars.tests.setup_data_car import SetUpCar
from cars.utils.for_views import create_slug

User = get_user_model()


def create_data_for_creating_car() -> dict:

    data = {
        'car_brand': SetUpCar.create_car_brand(),
        'car_model': SetUpCar.create_car_model(),
        'release_year': SetUpCar.create_car_release_year(),
        'reg_number': SetUpCar.create_car_reg_number(),
        'vin_code': SetUpCar.create_car_vin_code(length=17),
        'mileage': SetUpCar.create_car_mileage(),
    }
    data.update({
        'slug': create_slug(
            car_brand=data['car_brand'],
            car_model=data['car_model'],
            reg_number=data['reg_number']
        )
    })
    return data


print(create_data_for_creating_car())

# import random
# from users.tests.setup_data import SetUp
#
#
# def collecting_data_for_creating_users() -> dict:
#     main_data = {
#         'email': SetUp.create_email(),
#         'phone_number': SetUp.create_phone_number(),
#         'password': '3816069Lms',
#     }
#
#     additional_data = ['first_name', 'last_name', 'username']
#     temp_dict = {}
#     num_elements = random.randint(1, 3)
#
#     for i in range(int(num_elements)):
#         data = random.choices(additional_data)[0]
#         if data == 'first_name':
#             temp_dict.setdefault('first_name', SetUp.create_first_name())
#         elif data == 'last_name':
#             temp_dict.setdefault('last_name', SetUp.create_last_name())
#         elif data == 'username':
#             temp_dict.setdefault('username', SetUp.create_username())
#
#     data_for_creating_users = {**main_data, **temp_dict}
#     return data_for_creating_users
