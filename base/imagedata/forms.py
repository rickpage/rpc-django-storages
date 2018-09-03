from django import forms

from base.imagedata.models import ImageData


class ImageDataForm(forms.ModelForm):
    class Meta:
        model = ImageData
