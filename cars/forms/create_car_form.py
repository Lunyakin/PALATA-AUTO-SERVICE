from django import forms

from cars.models import Cars


class CreateCarForm(forms.ModelForm):
    car_brand = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'}
        ),
        label='Car brand',
        label_suffix='',
        required=True
    )
    car_model = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'}
        ),
        label='Car model',
        label_suffix='',
        required=True
    )
    release_year = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'}
        ),
        label='Release year',
        label_suffix='',
        required=True
    )
    reg_number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'}
        ),
        label='Registration number',
        label_suffix='',
        required=True
    )
    vin_code = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'}
        ),
        label='Vin code',
        label_suffix='',
        required=True
    )
    mileage = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'}
        ),
        label='Mileage',
        label_suffix='',
        required=True
    )
    car_photo = forms.ImageField(
        widget=forms.FileInput(
            attrs={'class': 'form-control'}
        ),
        label='Car photo',
        label_suffix='',
        required=False
    )

    class Meta:
        model = Cars
        fields = ('car_brand', 'car_model', 'release_year', 'reg_number', 'vin_code', 'mileage', 'car_photo')

    def clean_release_year(self):
        data = self.cleaned_data['release_year']
        if data.isdigit() and len(data) == 4:
            return data
        else:
            raise forms.ValidationError('Неверно указан год.')

    def clean_mileage(self):
        data = self.cleaned_data['mileage']
        if data.isdigit():
            return data
        else:
            raise forms.ValidationError('Неверно указан пробег.')

    def clean_reg_number(self):
        return self.cleaned_data['reg_number'].upper()

    def clean_vin_code(self):
        data = self.cleaned_data['vin_code']
        if len(data) == 17:
            return data
        else:
            error = f'Братан, проверь винкод. Егодлина должна быть 17 символов, а ты ввел {len(data)}'
            raise forms.ValidationError(error)
