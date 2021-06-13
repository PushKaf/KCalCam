from django import forms
from .models import Image


class FormImage(forms.ModelForm):
    class Meta:
        model = Image
        fields=("userImage",)