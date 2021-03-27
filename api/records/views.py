from rest_framework import viewsets, status
from .serializers import CallRecordSerializer#, BillSerializer
from .models import CallRecord#, Bill
from rest_framework.response import Response
from rest_framework.decorators import action


class CallRecordViewSet(viewsets.ModelViewSet):
    queryset = CallRecord.objects.all()
    serializer_class = CallRecordSerializer

    

    def create(self, request, *args, **kwargs):
        print(request.data)
        if request.data.get('type') == 'start':
            request.data['start_call'] = request.data['timestamp']
            print('aqui')
        else:
            print('tilt')
            return Response(status=status.HTTP_403_FORBIDDEN)

        serializer = self.get_serializer(data=request.data)
        print(serializer)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


    def partial_update(self, request, *args, **kwargs):
        # instance = self.queryset.get(pk=kwargs.get('pk'))
        if request.data.get('type') == 'end':
            request.data['end_call'] = request.data['timestamp']
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
        instance = self.queryset.get(call_id=request.data.get('call_id'))
        print(f'{instance=}')
        serializer = self.serializer_class(instance, data=request.data, partial=True)
        print(f'{request.data=}')
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


# class BillViewSet(viewsets.ModelViewSet):
#     queryset = Bill.objects.all()
#     serializer_class = BillSerializer


# modificar comportamentos
     