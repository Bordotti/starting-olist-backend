from .models import CallRecord, Bill
from rest_framework import serializers


class CallRecordSerializer(serializers.ModelSerializer):

    duration = serializers.SerializerMethodField()

    class Meta:
        model = CallRecord
        fields = (
            'id',
            'initial_call',
            'end_call',
            'source',
            'destination',
            'duration'
        )

    def get_duration(self, obj):
        duration = obj.end_call - obj.initial_call
        return duration.total_seconds()


class BillSerializer(serializers.ModelSerializer):

    duration = serializers.SerializerMethodField()

    class Meta:
        model = Bill
        fields = (
            'id',
            'source',
            # 'initial_call',
            # 'duration'
            # 'price'
        )

    # def get_duration(self, obj):
    #     duration = obj.end_call - obj.initial_call
    #     return duration.total_seconds()
