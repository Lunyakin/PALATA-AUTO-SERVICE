from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django import forms

User = get_user_model()


class LoginForm(AuthenticationForm):
    username = forms.EmailField()
    password = forms.CharField(
        strip=False,
    )

    error_messages = {
        "invalid_login": (
            "Пожалуйста введи корректный %(username)s и пароль. Заметь, что  "
            "поля чувствительный к регистру"
        ),
        "inactive": "Этот аккаунт не активен",
    }

    class Meta:
        model = User
