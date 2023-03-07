from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from datetime import datetime
from cloudinary.models import CloudinaryField

from django.urls import reverse


# Database columns are here!!

# Category table
# The categories for the project are: 
# Household, Work, Health, Childcare, Private_time, Other
class Task_Category(models.Model):
    name = models.CharField(max_length=100)
    featured_image = CloudinaryField('image', default='placeholder')  # noqa

    def __str__(self):
        return self.name


# Task table
class Mom_task(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='momtask')  # noqa
    featured_image = CloudinaryField('image', default='placeholder')  # noqa
    title = models.CharField(max_length=50, null=False, blank=False)
    complete = models.BooleanField(null=False, blank=False, default=False)
    description = models.TextField(max_length=500)
    category = models.ForeignKey(Task_Category, null=False, blank=False, on_delete=models.CASCADE)  # noqa
    start_time = models.DateField()
    end_time = models.DateField()

    class Meta:
        ordering = ['start_time']

    def __str__(self):
        return self.title

    # this is for having task titles inside the calendar view
    @property
    def get_html_url(self):
        url = reverse('edit', args=(self.id,))
        return f'<a  style="color: brown; font-weight: 500;" href="{url}"> {self.title} </a>'  # noqa


# Contact Form table
class Mom_contact(models.Model):
    email = models.EmailField(max_length=50, null=False, blank=False)
    topic = models.CharField(max_length=50, null=False, blank=False)
    your_message = models.CharField(max_length=300)

    def __str__(self):
        return self.topic
