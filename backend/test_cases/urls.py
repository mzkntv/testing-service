from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register(r'test-cases', views.TestCaseViewSet, 'test_cases')

urlpatterns = []
urlpatterns += router.urls
