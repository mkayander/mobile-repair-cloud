from rest_framework import serializers

from web.models import Visitor


class VisitorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Visitor
        fields = '__all__'
