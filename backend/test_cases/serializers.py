from rest_framework.serializers import ModelSerializer

from . import models


class TestCaseSerializer(ModelSerializer):
    class Meta:
        model = models.TestCase
        fields = '__all__'
