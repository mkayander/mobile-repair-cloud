from rest_framework import serializers

from web.models import Visitor, FeedbackRequest, GalleryPhoto


class VisitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitor
        fields = '__all__'


class FeedbackRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackRequest
        fields = '__all__'


class GalleryPhotoSerializer(serializers.ModelSerializer):
    height = serializers.IntegerField(source="image.height", read_only=True)
    width = serializers.IntegerField(source="image.width", read_only=True)

    class Meta:
        model = GalleryPhoto
        fields = '__all__'
