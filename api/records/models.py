from django.db import models


class CallRecord(models.Model):

    type_choice = (('START', 'start at'), ('END', 'end at'))

    type_call = models.CharField(max_length=50, choices=type_choice)
    timestamp = models.DateTimeField(auto_now_add=True)
    call_id = models.CharField(max_length=64)
    source = models.CharField(max_length=13)
    destination = models.CharField(max_length=13)

    class Meta:
        unique_together = ('call_id', 'type_call')


# class StartCallRecorder(CallRecord):
#     def __init__(self, type_call, timestamp, call_id, source, destination):
#         super().__init__(type_call, timestamp, call_id)
#         self.source = models.CharField(max_length=13)
#         self.destination = models.CharField(max_length=13)

# class EndCallRecorder(CallRecord):
#     def __init__(self, type_call, timestamp, call_id)

