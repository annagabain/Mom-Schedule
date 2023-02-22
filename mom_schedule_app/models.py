from django.db import models
from django.contrib.auth.models import User

import datetime


# Database columns are here!!

# Task table
class Mom_task(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="momtask")  # noqa
    title = models.CharField(max_length=50, null=False, blank=False)
    complete = models.BooleanField(null=False, blank=False, default=False)
    # category = models.ForeignKey(Mom_category, null=True, on_delete=models.CASCADE, related_name="momtask")  # noqa
    description = models.TextField(max_length=500)
    date = models.DateField()

    def __str__(self):
        return self.title


# Category table
# class Mom_category(models.Model):
#   name = models.CharField(max_length=50, null=False)
    # def __str__(self):
    #     return self.name

    # Household
    # Work
    # Childcare
    # Private_time
    # Other


# Contact Form table
class Mom_contact(models.Model):
    email = models.EmailField(max_length=50, null=False, blank=False)
    topic = models.CharField(max_length=50, null=False, blank=False)
    your_message = models.CharField(max_length=300)

    def __str__(self):
        return self.topic
