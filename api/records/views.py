from rest_framework import viewsets, status
from .serializers import CallRecordSerializer
from .models import CallRecord
from rest_framework.response import Response


class CallRecordViewSet(viewsets.ModelViewSet):
    queryset = CallRecord.objects.all()
    serializer_class = CallRecordSerializer




# class BillViewSet(viewsets.ModelViewSet):
#     queryset = Bill.objects.all().order_by('start')
#     serializer_class = BillSerializer

#     def create(self, request):
#         data = request.data
#         start = data.get('start')
#         end = data.get('end')
#         print(start, end)
#         return Response(status = status.HTTP_200_OK)
