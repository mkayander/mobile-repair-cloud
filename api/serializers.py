from rest_framework import serializers

from web.models import Visitor, FeedbackRequest


class VisitorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Visitor
        fields = '__all__'


class FeedbackRequestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FeedbackRequest
        fields = '__all__'
