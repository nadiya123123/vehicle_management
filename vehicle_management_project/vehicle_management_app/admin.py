from django.contrib import admin
from .models import Vehicle

class VehicleAdmin(admin.ModelAdmin):
    list_display = ('vehicle_number', 'vehicle_type', 'vehicle_model', 'vehicle_description')
    list_filter = ('vehicle_type',)
    search_fields = ('vehicle_number', 'vehicle_model', 'vehicle_description')

admin.site.register(Vehicle, VehicleAdmin)