from django.urls import include, path
from rest_framework import routers
from .views import CallRecordViewSet


router = routers.DefaultRouter()
router.register(r'CallRecord', CallRecordViewSet, basename="CallRecord")
# router.register(r'EndCallRecord', EndCallRecordViewSet, basename="EndCallRecord")
# router.register(r'Bill', BillViewSet, basename="Bill")

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include(
        'rest_framework.urls', namespace='rest_framework'))
]
