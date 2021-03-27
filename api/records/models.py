from django.db import models

class CallRecord(models.Model):

    call_id = models.IntegerField()
    start_call = models.DateTimeField(null=True, blank=True)
    end_call = models.DateTimeField(null=True, blank=True)
    source = models.CharField(max_length=13, null=True, blank=True)
    destination = models.CharField(max_length=13, null=True, blank=True)

    # class Meta:
    #     unique_together = ('start_call', 'source')

    def __str__(self):
        return f"Start_call {self.start_call} | End_call {self.end_call} | Id {self.call_id} | Source: {self.source} | Destination: {self.destination}"


# class Bill(models.Model):
    ###filtro em vez de uma model com dropdown, a pessoa digita o telefone dela
    # source = models.ForeignKey(CallRecord, related_name='source_bill', on_delete=models.CASCADE)
    # initial_call = models.ForeignKey(CallRecord, related_name='initial_call_bill', on_delete=models.CASCADE)

    # class Meta:
    #     unique_together = ('source', 'initial_call')
