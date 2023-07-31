from faker import Faker

fake = Faker()
fake_phone_number = Faker('Uk_UA')


class SetUpUser:
    @staticmethod
    def create_email():
        first_pat = fake.lexify(text='??????????')
        first_pat = first_pat.lower()
        second_part = '@gmail.com'
        return first_pat + second_part

    @staticmethod
    def create_first_name():
        return fake.first_name()

    @staticmethod
    def create_last_name():
        return fake.last_name()

    @staticmethod
    def create_password():
        return fake.lexify(text='????????')

    @staticmethod
    def create_phone_number():
        return fake_phone_number.phone_number()

    @staticmethod
    def create_username():
        return fake.simple_profile()['username']
