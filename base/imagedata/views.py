from django.shortcuts import render
from django.views.generic import CreateView

from base.imagedata.forms import ImageDataForm

class ImageDataCreateView(CreateView):
    form_class = ImageDataForm
