from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class EditUserForm(forms.ModelForm):
    username = forms.CharField(
        required=False
    )
    email = forms.EmailField(
        error_messages={
            'invalid': 'Введите корректный адрес'
        }
    )
    first_name = forms.CharField(
        required=False
    )
    last_name = forms.CharField(
        required=False
    )
    photo = forms.ImageField(
        required=False
    )
    phone_number = forms.CharField(
        required=False
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'phone_number', 'photo')
