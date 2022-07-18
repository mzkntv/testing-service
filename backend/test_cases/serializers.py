from rest_framework import serializers

from . import models


class TestCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TestCase
        fields = '__all__'


class ProcessingTestCaseSerializer(serializers.ModelSerializer):
    started_at = serializers.DateTimeField(label='Дата начала прохождения теста', read_only=True)
    status = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = models.ProcessingTestCase
        fields = ('id', 'test_case', 'started_at', 'status', 'current_question',)


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Choice
        fields = ('id', 'text',)


class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)

    class Meta:
        model = models.Question
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    next_question = serializers.PrimaryKeyRelatedField(
        read_only=True,
        source='question.next_question',
    )
    selected_choices = serializers.PrimaryKeyRelatedField(
        many=True,
        write_only=True,
        queryset=models.Choice.objects.all()
    )

    class Meta:
        model = models.Answer
        fields = '__all__'
