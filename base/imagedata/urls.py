from django.conf.urls import include, url
from django.contrib import admin

from imagedata.views import ImageDataCreateView

urlpatterns = [
    url(r'^/', ImageDataCreateView.as_view(), name="create"),
]
