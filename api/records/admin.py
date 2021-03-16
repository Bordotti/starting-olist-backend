from django.contrib import admin
from .models import CallRecord


class CallRecordAdmin(admin.ModelAdmin):
    list_display = ('type_call', 'timestamp', 'call_id', 'source', 'destination')


admin.site.register(CallRecord, CallRecordAdmin)
