from django.db import models
from django.utils import timezone
from decimal import Decimal

class Guest(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Room(models.Model):
    ROOM_TYPES = [
        ('single', 'Single'),
        ('double', 'Double'),
        ('suite', 'Suite'),
    ]
    
    room_number = models.CharField(max_length=10, unique=True)
    room_type = models.CharField(max_length=10, choices=ROOM_TYPES)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Room {self.room_number} ({self.get_room_type_display()})"

class Staff(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    role = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.role}"

class Reservation(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        days_stayed = (self.check_out_date - self.check_in_date).days
        self.total_price = Decimal(days_stayed) * self.room.price_per_night
        self.room.is_available = False  # Mark the room as unavailable once reserved
        self.room.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Reservation for {self.guest} in {self.room}"

class Feedback(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    feedback = models.TextField()
    date_submitted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Feedback by {self.guest} for {self.reservation}"