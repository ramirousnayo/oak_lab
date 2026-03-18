from django.db import models
from django.contrib.auth.models import User

class Creature(models.Model):
    TYPES = [('fire','Fuego'), ('water', 'Agua'), ('grass', 'Planta')]
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=10, choices=TYPES)
    emoji = models.CharField(max_length=5)
    description = models.TextField()

class TimeSlot(models.Model):
    DAYS = [(0, 'Lunes'), (1, 'Martes'), (2, 'Miércoles'),
            (3, 'Jueves'), (4, 'Viernes')]
    day = models.IntegerField(choices=DAYS)
    start_time = models.TimeField()
    end_time = models.TimeField()
    capacity = models.PositiveIntegerField(default=3)

    def spots_left(self):
        return self.capacity - self.bookings.count()

class Booking(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='booking')
    creature = models.ForeignKey(Creature, on_delete=models.PROTECT)
    timeslot = models.ForeignKey(TimeSlot, on_delete=models.PROTECT,
                                 related_name='bookings')
    created_at = models.DateTimeField(auto_now_add=True)
