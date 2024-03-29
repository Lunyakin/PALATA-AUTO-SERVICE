from django.test import TestCase
from users.forms.registration_form import RegistrationForm
from users.tests.setup_data_user import SetUpUser


class TestRegistrationsForm(TestCase):
    def setUp(self):
        self.password = SetUpUser.create_password()
        self.email = SetUpUser.create_email()
        self.phone_number = '+380506468202'

    def test_registrations_form_is_valid(self):
        data = {
            'email': self.email,
            'phone_number': self.phone_number,
            'password1': self.password,
            'password2': self.password,
        }

        form = RegistrationForm(data)
        self.assertTrue(form.is_valid())

    def test_registrations_form_is_no_valid(self):
        data = {
            'email': self.email,
            'phone_number': self.phone_number,
            'password1': self.password,
            'password2': 'incorrect password'
        }
        form = RegistrationForm(data)
        self.assertFormError(form, 'password2', 'Пароли не совпадают.')
