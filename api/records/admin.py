from django.contrib import admin
from .models import CallRecord

@admin.register(CallRecord)
class CallRecordAdmin(admin.ModelAdmin):
    list_display = ('initial_call', 'end_call', 'source', 'destination')


# @admin.register(EndCallRecord)
# class EndCallRecordAdmin(admin.ModelAdmin):
#     list_display = ('type_call', 'timestamp', 'call_id')

# admin.site.register(CallRecord, CallRecordAdmin)
