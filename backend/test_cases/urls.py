from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register(r'test-cases', views.TestCaseViewSet, 'test_cases')
router.register(r'processing-test-cases', views.ProcessingTestCaseViewSet, 'processing_test_cases')

urlpatterns = []
urlpatterns += router.urls
