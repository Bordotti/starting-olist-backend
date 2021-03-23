from rest_framework import viewsets, status
from .serializers import CallRecordSerializer, BillSerializer
from .models import CallRecord, Bill
from rest_framework.response import Response


class CallRecordViewSet(viewsets.ModelViewSet):
    queryset = CallRecord.objects.all()
    serializer_class = CallRecordSerializer


class BillViewSet(viewsets.ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
