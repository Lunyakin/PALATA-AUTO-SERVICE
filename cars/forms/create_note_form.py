from django import forms

from cars.models.car import Car


class CreateNoteForm(forms.Form):
    title = forms.CharField()
    descriptions = forms.CharField(
        required=False,
        widget=forms.Textarea
    )
    photo = forms.ImageField(required=False)


