from django.db import models


class CallRecord(models.Model):

    initial_call = models.DateTimeField()
    end_call = models.DateTimeField()
    source = models.CharField(max_length=13)
    destination = models.CharField(max_length=13)

    def __str__(self):
        return f"ID call: {self.id} | Source: {self.source} | Started at {self.initial_call}"

class Bill(models.Model):
    source = models.ForeignKey(CallRecord, related_name='source_bill', on_delete=models.CASCADE)
    # initial_call = models.ForeignKey(CallRecord, related_name='initial_call_bill', on_delete=models.CASCADE)

    # class Meta:
    #     unique_together = ('source', 'initial_call')