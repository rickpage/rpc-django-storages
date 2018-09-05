from rest_framework import serializers

from imagedata.models import Photo


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('creator', 'created', 'image', 'description' )
