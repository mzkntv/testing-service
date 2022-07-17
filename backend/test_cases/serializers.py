from rest_framework import serializers

from . import models


class TestCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TestCase
        fields = '__all__'


class ProcessingTestCaseSerializer(serializers.ModelSerializer):
    started_at = serializers.DateTimeField(label='Дата начала прохождения теста', read_only=True)
    status = serializers.CharField(source='get_status_display', read_only=True)
    current_question = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='api:questions-detail',
    )

    class Meta:
        model = models.ProcessingTestCase
        fields = ('id', 'test_case', 'started_at', 'status', 'current_question',)


class QuestionSerializer(serializers.ModelSerializer):
    next_question = serializers.HyperlinkedRelatedField(read_only=True, view_name='api:questions-detail')

    class Meta:
        model = models.Question
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    next_question = serializers.HyperlinkedRelatedField(
        read_only=True,
        source='question.next_question',
        view_name='api:questions-detail'
    )
    selected_choices = serializers.PrimaryKeyRelatedField(
        many=True,
        write_only=True,
        queryset=models.Choice.objects.all()
    )

    class Meta:
        model = models.Answer
        fields = '__all__'
