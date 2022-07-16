from rest_framework import viewsets

from . import models, serializers


class TestCaseViewSet(viewsets.ModelViewSet):
    queryset = models.TestCase.objects.all()
    serializer_class = serializers.TestCaseSerializer


class ProcessingTestCaseViewSet(viewsets.ModelViewSet):
    queryset = models.ProcessingTestCase.objects.all()
    serializer_class = serializers.ProcessingTestCaseSerializer

    def perform_create(self, serializer: serializers.ProcessingTestCaseSerializer) -> None:
        first_question = models.Question.objects.filter(
            test_case_id=serializer.validated_data['test_case'],
            is_first=True
        ).first()
        serializer.save(user=self.request.user, current_question=first_question)


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = models.Question.objects.all()
    serializer_class = serializers.QuestionSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = models.Answer.objects.all()
    serializer_class = serializers
