from django.contrib.auth import get_user_model
from django.test import TestCase
from users.tests.setup_data import SetUp


class TestUserModel(TestCase):
    def setUp(self):
        self.db = get_user_model()
        self.email = SetUp.create_email()
        self.phone_number = SetUp.create_phone_number()
        self.password = SetUp.create_password()
        self.first_name = SetUp.create_first_name()
        self.last_name = SetUp.create_last_name()
        self.username = SetUp.create_username()

    def test_create_super_user(self):
        super_user = self.db.objects.create_superuser(
            email=self.email, password=self.password
        )
        self.assertEqual(super_user.email, self.email)
        self.assertTrue(super_user.is_staff)
        self.assertTrue(super_user.is_superuser)
        self.assertEqual(str(super_user), self.email)

        with self.assertRaises(ValueError):
            self.db.objects.create_superuser(
                email='', password=self.password
            )

    def test_create_user(self):
        user = self.db.objects.create_user(
            email=self.email, password=self.password,
        )
        self.assertEqual(user.email, self.email)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertEqual(str(user), self.email)
        self.assertEqual(str(user.get_short_name()), self.email.split('@')[0])

    def test_str_method_username(self):
        user = self.db.objects.create_user(
            email=self.email, password=self.password,
            username=self.username
        )
        self.assertEqual(str(user), self.username)

    def test_str_method_get_full_name(self):
        user = self.db.objects.create_user(
            email=self.email, password=self.password,
            username=self.username, last_name=self.last_name, first_name=self.first_name
        )
        self.assertEqual(str(user), f'{user.first_name} {user.last_name}')
        self.assertEqual(str(user.get_short_name()), f'{user.first_name}')
