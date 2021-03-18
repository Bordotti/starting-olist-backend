from .models import CallRecord
from rest_framework import serializers


class CallRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallRecord
        fields = '__all__'



# class BillSerializer(serializers.ModelSerializer):
#     duration = serializers.DurationField(read_only = True)
    
#     class Meta:
#         model = Bill
#         fields = '__all__'
#         # fields = ('start', 'end')


