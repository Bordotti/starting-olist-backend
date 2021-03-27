from .models import CallRecord#, Bill
from rest_framework import serializers


class CallRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallRecord
        fields = (
            'id',
            'call_id',
            'start_call',
            'end_call',
            'source',
            'destination',
            # 'duration',
        )

    # def get_duration(self, obj):
    #     duration = obj.end_call - obj.start_call
    #     return duration.total_seconds()


# class BillSerializer(CallRecordSerializer):

    # start_call = CallRecordSerializer()
    # end_call = CallRecordSerializer()
    # duration = serializers.SerializerMethodField()

    # class Meta:
    #     model = Bill
    #     fields = (
    #         'id',
    #         'source',
            # 'start_call',
            # 'end_call,
            # 'duration' , #COMO VOU FAZER A DURAÇÃO COM O CÁLCULO DE CAMPOS DE OUTRO MODEL?
            # 'price'
        # )

    # def get_duration(self, start_call, end_call):
    #     duration = CallRecordSerializer(instance.end_call) - allRecordSerializer(instance.initial_call)
    #     return duration.total_seconds()
