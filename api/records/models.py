from django.db import models


class CallRecord(models.Model):

    initial_call = models.DateTimeField()
    end_call = models.DateTimeField()
    # duration = models.DurationField()
    source = models.CharField(max_length=13)
    destination = models.CharField(max_length=13)

    def __str__(self):
        return f"ID call: {self.id} | Started at {self.initial_call} | \
            Ended at {self.end_call} | Source: {self.source} \
                | Destination {self.destination}"
