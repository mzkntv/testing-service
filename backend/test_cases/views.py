from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from . import models, serializers


class TestCaseViewSet(viewsets.ModelViewSet):
    queryset = models.TestCase.objects.all()
    serializer_class = serializers.TestCaseSerializer

    @action(methods=['POST'], detail=True)
    def start(self, request: Request, *args, **kwargs) -> Response:
        ...


class ProcessingTestCaseViewSet(viewsets.ModelViewSet):
    ...
