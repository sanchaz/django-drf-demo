from rest_framework import serializers

from .models import DemoModel


class DemoSerializer(serializers.ModelSerializer):

    class Meta:
        model = DemoModel
        fields = ('field1', 'field2')


class AnotherSerializer(serializers.Serializer):
    field100 = serializers.BooleanField()
    field200 = serializers.CharField()
