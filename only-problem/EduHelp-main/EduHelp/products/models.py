# models.py
from django.db import models
from django.utils.timezone import now

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="Course")
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    video = models.FileField(upload_to='lectures/videos/', null=True, blank=True)
    ebook = models.FileField(upload_to='lectures/notes/')
    image = models.ImageField(upload_to='lectures/images/', null=True, blank=True)
    created_at = models.DateTimeField(default=now)  # New field to track creation time

    def __str__(self):
        return self.name
    





