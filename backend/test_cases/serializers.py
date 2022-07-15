from datetime import datetime

from rest_framework import serializers

from . import models


class TestCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TestCase
        fields = '__all__'


class ProcessingTestCaseSerializer(serializers.ModelSerializer):
    started_at = serializers.DateTimeField(label='Дата начала прохождения теста', read_only=True)
    status = serializers.CharField(source='get_status_display')

    class Meta:
        model = models.ProcessingTestCase
        fields = ('test_case', 'started_at', 'status', 'current_question',)
