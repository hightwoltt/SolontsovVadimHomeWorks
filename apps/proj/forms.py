
from unicodedata import category
from django import forms

from .models import Homework
from auths.models import CustomUser

class CreateHomeworkForm(forms.ModelForm):

    user = forms.ModelChoiceField(
        queryset=CustomUser.objects.all(),
        widget=forms.Select()
    )

    title = forms.CharField(
        label='Название',
        widget=forms.TextInput(),
    )

    subject = forms.CharField(
        label='Предмет',
        widget=forms.TextInput(),
    )

    logo = forms.ImageField(
        label='Лого',
        widget=forms.FileInput(),
    )

    class Meta:
        model = Homework
        fields = (
            'title',
            'subject',
            'logo',
            'user',
        )