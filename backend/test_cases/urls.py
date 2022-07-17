from rest_framework import routers
from rest_framework_nested import routers as nested_routers

from . import views

app_name = 'test_case'

router = routers.SimpleRouter()
router.register(r'test-cases', views.TestCaseViewSet, 'test_cases')

test_case_router = nested_routers.NestedSimpleRouter(router, r'test-cases', lookup='test_case')
test_case_router.register(r'processing', views.ProcessingTestCaseViewSet, 'processing_test_cases')

router.register(r'questions', views.QuestionViewSet, 'questions')
router.register(r'answer', views.AnswerViewSet, 'answer')

urlpatterns = []
urlpatterns += router.urls
urlpatterns += test_case_router.urls
