from django.db import models


class CallRecord(models.Model):
    # type_choice = (('START', 'start at'), ('END', 'end at'))

    # type_call = models.CharField(max_length=50, choices=type_choice)
    # timestamp = models.DateTimeField(auto_now_add=True)
    # call_id = models.CharField(max_length=64)
    initial_call = models.DateTimeField()
    end_call = models.DateTimeField()
    source = models.CharField(max_length=13)
    destination = models.CharField(max_length=13)

    def __str__(self):
        return f"ID call: {seld.id} | Started at {self.initial_call} | \
            Ended at {self.end_call} | Source: {self.source} | Destination {self.destination}"


    # class Meta:
    #     unique_together = ('call_id', 'type_call')
#1 classe só contendo início e fim da chamada
#call_id tira


# class Bill(models.Model):
#     destination = models.ForeignKey(StartCallRecord, related_name='destination_call_bill', on_delete=models.CASCADE)
#     start = models.ForeignKey(StartCallRecord, related_name='start_call_bill', on_delete=models.CASCADE)
#     end = models.ForeignKey(EndCallRecord, related_name='end_call_bill', on_delete=models.CASCADE)
#     price = models.DecimalField(max_digits=5, decimal_places=2)

#     # @property
#     # def start_date(self):
#     #     return self.start_record.timestamp.date()

#     # @property
#     # def start_time(self):
#     #     return self.start_record.timestamp.time()

#     @property
#     def duration(self):
#         if not (self.start and self.end): 
#             return None
#         a, b = self.start, self.end
#         return '%s:%s' % ((b-a).days*24 + (b-a).seconds//3600, (b-a).seconds%3600//60)
