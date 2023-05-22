from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from users.utils.for_models import path_for_users_foto


class Role(models.TextChoices):
    """Роли пользователя"""
    MANAGER = 'MANAGER', 'Менеджер'
    CUSTOMER = 'CUSTOMER', 'Клиент'


class MyUserManager(BaseUserManager):
    """Создание и сохранение User по email и паролю """

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('У пользователя должен быть электронный адрес')

        user = self.model(
            email=self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """Расширение абстрактного юзера"""
    email = models.EmailField(
        "Почта",
        unique=True,
        error_messages={
            "unique": "Пользователь с таким email уже существует",
        }
    )
    username = models.CharField(
        "Ник нейм",
        max_length=150,
        unique=False,
        blank=True
    )
    phone_number = PhoneNumberField(
        unique=True,
        verbose_name='Номер телефона'
    )
    photo = models.ImageField(
        upload_to=path_for_users_foto,
        blank=True,
        null=True,
        verbose_name='Фотография'

    )
    last_login = models.DateTimeField(blank=True, null=True)  # TODO настроить время! отстает на 3 часа

    role = models.CharField(
        max_length=15,
        choices=Role.choices,
        default=Role.CUSTOMER
    )

    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пациент'
        verbose_name_plural = 'Пациенты'

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_short_name(self):
        return self.first_name or self.email.split('@')[0]

    def __str__(self):
        if self.first_name and self.last_name:
            return self.get_full_name()
        elif self.username:
            return self.username
        else:
            return f'{self.email}'
