from rest_framework import serializers

from pricing.models import Brand, DeviceModel, Service
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


class DeviceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceModel
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    models = DeviceModelSerializer(many=True, read_only=True)

    class Meta:
        model = Brand
        fields = ['name', 'logo', 'models']


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
