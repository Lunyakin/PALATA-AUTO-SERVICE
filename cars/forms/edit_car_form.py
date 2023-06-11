from django import forms
from cars.models import Cars


class EditCarForm(forms.ModelForm):
    reg_number = forms.CharField(
        required=False
    )
    car_photo = forms.ImageField(
        required=False
    )

    class Meta:
        model = Cars
        fields = ('reg_number', 'car_photo',)

    def clean_reg_number(self):
        return self.cleaned_data['reg_number'].upper()
