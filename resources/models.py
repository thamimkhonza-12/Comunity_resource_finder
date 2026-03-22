from django.db import models
from locations.models import Location
from django.db.models import Avg

class Resource(models.Model):
    CATEGORY_CHOICES = [
        ('clinic', 'Clinic'),
        ('shelter', 'Shelter'),
        ('food', 'Food Bank'),
        ('education', 'Education'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    contact_phone = models.CharField(max_length=20, blank=True)
    contact_email = models.EmailField(blank=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

        from django.db.models import Avg

@property
def average_rating(self):
    return self.review_set.aggregate(avg=Avg('rating'))['avg'] or 0

@property
def review_count(self):
    return self.review_set.count()