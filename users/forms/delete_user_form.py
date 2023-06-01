from django import forms


class DeleteUserForm(forms.Form):

    agreement = forms.BooleanField(required=True)
