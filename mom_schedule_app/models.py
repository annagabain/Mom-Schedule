from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from datetime import datetime
from cloudinary.models import CloudinaryField

from django.urls import reverse


# Database columns are here!!

# Category table
class Task_Category(models.Model):
    name = models.CharField(max_length=100)
    featured_image = CloudinaryField('image', default='placeholder')  # noqa

    def __str__(self):
        return self.name

    # Household
    # Work
    # Childcare
    # Private_time
    # Other


# Task table
class Mom_task(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="momtask")  # noqa
    featured_image = CloudinaryField('image', default='placeholder')  # noqa
    title = models.CharField(max_length=50, null=False, blank=False)
    complete = models.BooleanField(null=False, blank=False, default=False)
    description = models.TextField(max_length=500)
    category = models.ForeignKey(Task_Category, null=False, blank=False, on_delete=models.CASCADE)  # noqa
    # date = models.DateField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    class Meta:
        ordering = ['start_time']

    def __str__(self):
        return self.title


# Contact Form table
class Mom_contact(models.Model):
    email = models.EmailField(max_length=50, null=False, blank=False)
    topic = models.CharField(max_length=50, null=False, blank=False)
    your_message = models.CharField(max_length=300)

    def __str__(self):
        return self.topic
