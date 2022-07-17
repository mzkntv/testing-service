from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

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

    @action(methods=['GET'], detail=True)
    def result(self, request: Request, *args, **kwargs) -> Response:
        instance: models.ProcessingTestCase = self.get_object()
        if instance.status != models.ProcessingTestCase.COMPLETED_STATE_CHOICE:
            return Response(
                data={
                    'error': 'Test case must be completed to see results'
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        question_counter = 0
        correct_question_counter = 0
        for answer in instance.answer_set.all():
            question_counter += 1
            if set(answer.selected_choices.all()) == set(answer.question.choices.filter(is_correct=True)):
                correct_question_counter += 1

        return Response(
            status=status.HTTP_200_OK,
            data={
                'correct_answers': correct_question_counter,
                'all_answers': question_counter,
                'percent': correct_question_counter / question_counter * 100
            }
        )


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = models.Question.objects.all()
    serializer_class = serializers.QuestionSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = models.Answer.objects.all()
    serializer_class = serializers.AnswerSerializer

    def perform_create(self, serializer: serializers.AnswerSerializer) -> None:
        question = serializer.validated_data['question']
        processing_test_case = serializer.validated_data['processing_test_case']
        if question.next_question is None:
            processing_test_case.status = models.ProcessingTestCase.COMPLETED_STATE_CHOICE
        processing_test_case.current_question = question.next_question
        serializer.save()
        question.save()
