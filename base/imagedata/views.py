from django.views.generic import CreateView
from imagedata.models import ImageData, Photo


class ImageDataCreateView(CreateView):
    model = ImageData
    fields = ['image', 'caption', 'description']
    success_url = '/photos/imagedata/'


class PhotoCreateView(CreateView):
    model = Photo
    fields = ['creator', 'image', 'description']
    success_url = '/photos/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["photos"] = Photo.objects.all()
        return context