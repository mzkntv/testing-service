from rest_framework import viewsets

from . import models, serializers


class TestCaseViewSet(viewsets.ModelViewSet):
    queryset = models.TestCase.objects.all()
    serializer_class = serializers.TestCaseSerializer


class ProcessingTestCaseViewSet(viewsets.ModelViewSet):
    queryset = models.ProcessingTestCase.objects.all()
    serializer_class = serializers.ProcessingTestCaseSerializer

    def perform_create(self, serializer: serializers.ProcessingTestCaseSerializer) -> None:
        serializer.save(user=self.request.user)
