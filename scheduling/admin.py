from django.contrib import admin
from .models import Creature, TimeSlot, Booking

@admin.register(Creature)
class CreatureAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'emoji']

@admin.register(TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ['get_day_display', 'start_time', 'end_time', 'capacity', 'spots_left']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['user', 'creature', 'timeslot', 'created_at']
    ordering = ['-created_at']
