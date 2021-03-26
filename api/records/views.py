from rest_framework import viewsets, status
from .serializers import CallRecordSerializer#, BillSerializer
from .models import CallRecord#, Bill
from rest_framework.response import Response
from rest_framework.decorators import action


class CallRecordViewSet(viewsets.ModelViewSet):
    queryset = CallRecord.objects.all()
    serializer_class = CallRecordSerializer

    def partial_update(self, request, *args, **kwargs):
        # instance = self.queryset.get(pk=kwargs.get('pk'))
        instance = self.queryset.get(call_id=request.data.get('call_id'))
        print(self.queryset)
        serializer = self.serializer_class(instance, data=request.data, partial=True)
        print(request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


# class BillViewSet(viewsets.ModelViewSet):
#     queryset = Bill.objects.all()
#     serializer_class = BillSerializer


# modificar comportamentos
     