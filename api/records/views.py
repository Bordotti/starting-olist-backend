from rest_framework import viewsets, status
from .serializers import CallRecordSerializer
from .models import CallRecord
from rest_framework.response import Response


class CallRecordViewSet(viewsets.ModelViewSet):
    queryset = CallRecord.objects.all()
    serializer_class = CallRecordSerializer
