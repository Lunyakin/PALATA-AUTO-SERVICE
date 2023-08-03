from faker import Faker
from faker_vehicle import VehicleProvider

fake = Faker()
fake.add_provider(VehicleProvider)


class SetUpCar:

    @staticmethod
    def create_car_brand():
        return fake.vehicle_make()

    @staticmethod
    def create_car_model():
        return fake.vehicle_model()

    @staticmethod
    def create_car_release_year():
        return fake.vehicle_year()

    @staticmethod
    def create_car_reg_number():
        reg_number = f'{fake.pystr(min_chars=2, max_chars=2)}' \
                     f'{fake.pyint(min_value=1000, max_value=9999)}' \
                     f'{fake.pystr(min_chars=2, max_chars=2)}'
        return reg_number.upper()

    @staticmethod
    def create_car_vin_code(length: int):
        return fake.pystr(min_chars=length, max_chars=length)

    @staticmethod
    def create_car_mileage():
        return fake.pyint(min_value=20_000, max_value=500_000)
