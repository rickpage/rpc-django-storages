from django.conf.urls import include, url
from django.contrib import admin

from imagedata.views import ImageDataCreateView, PhotoCreateView

urlpatterns = [
    url(r'^imagedata$', ImageDataCreateView.as_view(), name="create"),
    url(r'^', PhotoCreateView.as_view(), name="photo-create"),
]
