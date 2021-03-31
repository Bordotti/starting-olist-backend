from rest_framework import viewsets, status
from .serializers import CallRecordSerializer#, BillSerializer
from .models import CallRecord#, Bill
from django.shortcuts import get_list_or_404
from rest_framework.response import Response
from rest_framework.decorators import action

from datetime import datetime, date, time, timedelta

class CallRecordViewSet(viewsets.ModelViewSet):
    queryset = CallRecord.objects.all()
    serializer_class = CallRecordSerializer

    def create(self, request, *args, **kwargs):
        if request.data.get('type', '').lower() == 'start':
            request.data['start_call'] = request.data['timestamp']
        else:
            return Response('This should be a start type, check for inconsistences', status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


    def partial_update(self, request, *args, **kwargs):
        if request.data.get('type', '').lower() == 'end':
            request.data['end_call'] = request.data['timestamp']
        else:
            return Response('This should be a end type, check for inconsistences', status=status.HTTP_400_BAD_REQUEST)
        instance = self.queryset.get(call_id=request.data.get('call_id'))
        
        # PROIBE UM END CALL MENOR QUE O START CALL
        if instance.start_call > request.data['end_call']:
            return Response('This should be a end type, check for inconsistences', status=status.HTTP_403_FORBIDDEN)
        
        serializer = self.serializer_class(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


CALL_STANDING_CHARGE = 0.36
CALL_MIN_CHARGE = 0.09

class BillViewSet(viewsets.ModelViewSet):
    def create(self, request):
        data = request.data
        source = data.get('source')
        period = data.get('period')
        bill = {'total_price': 00.00, 'source': source,
                'period': period, 'call_record': []}
        print(data)
        if not source:
            return Response("Invalid request. Missing source",
                            status=status.HTTP_400_BAD_REQUEST)

        if period:
            queryset = CallRecord.objects.filter(source=source).filter(
                end_call__year=period.split('/')[1],
                end_call__month=period.split('/')[0])
        else:
            default_date = date.today().replace(day=1) - timedelta(days=1)
            bill['period'] = f'{default_date.month}/{default_date.year}'
            queryset = CallRecord.objects.filter(source=source).filter(
                end_call__year=default_date.year,
                end_call__month=default_date.month)

        list_call = get_list_or_404(queryset)

        for call in list_call:
            print(call)
            
            destination = call.destination
            start_date = call.start_call.date().strftime('%d/%b/%Y')
            start_time = call.start_call.time()
            duration = call.end_call - call.start_call
            price = self.get_call_rec_price(
                call.start_call, call.end_call, duration)

            call_record = {
                'destination': destination, 'start_call_date': start_date,
                'start_call_time': start_time, 'duration': str(duration),
                'price': round(price, 2)}

            bill['total_price'] += price
            bill['call_record'].append(call_record)

        return Response(data=bill, status=status.HTTP_200_OK)


    def get_call_rec_price(self, start_call, end_call, duration):
        # A partir das 22h: sem custo por minuto
        # A partir das 06h: 0.09$ por minuto
        total_charge = CALL_STANDING_CHARGE


        if 6 <= start_call.hour < 22:
            if end_call.hour >= 22:
                time_diff = datetime.combine(start_call.date(), time(22,00)).replace(tzinfo=None) - start_call.replace(tzinfo=None)
                total_charge += CALL_MIN_CHARGE * int(time_diff.total_seconds()/60)
            elif start_call.hour < end_call.hour:
                total_charge += CALL_MIN_CHARGE *int(duration.total_seconds()/60)
        else:
            if 22 >= end_call.hour >= 6:

                time_diff = end_call.replace(tzinfo=None) - datetime.combine(end_call.date(), time(6,00)).replace(tzinfo=None)
                total_charge += CALL_MIN_CHARGE * int(time_diff.total_seconds()/60)
            else:
                if 24 <= duration.total_seconds()/60/60 >= 8:
                    # 29/03/21 5:44
                    # 29/03/21 22:20
                     total_charge += CALL_MIN_CHARGE * 16 * 60 # 16h do dia * 60 minutos
    
        return total_charge
                
