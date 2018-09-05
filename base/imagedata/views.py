from django.views.generic import CreateView
from rest_framework import viewsets

from imagedata.models import ImageData, Photo
from imagedata.serializers import PhotoSerializer


def set_routes(router):
    router.register(r'photo', PhotoSerializerViewSet)


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


class PhotoSerializerViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all().order_by('-created')
    serializer_class = PhotoSerializer

    def perform_create(self, serializer):
        from pdb import set_trace
        set_trace()
        serializer.save(creator=self.request.user)
