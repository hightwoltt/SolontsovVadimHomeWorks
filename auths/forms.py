from dataclasses import field
from django.contrib.auth.forms import(
    UserCreationForm,
    UserChangeForm,
)
from .models import CustomUser
from django import forms


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = (
            'email',
        )

class CustomUserChangeForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = (
            'email',
        )

class CustomUserForm(forms.ModelForm):
    email = forms.EmailField()
    password = forms.CharField(
        widget=forms.PasswordInput
    )

    class Meta:
        model = CustomUser
        fields = (
            'email',
            'password'
        )