from django.db import models
from django.contrib.auth.models import User

import datetime


# Database columns are here!!

# Task table
class Mom_task(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="momtask")  # noqa
    title = models.CharField(max_length=50, null=False, blank=False)
    complete = models.BooleanField(null=False, blank=False, default=False)
    # starred
    # category = models.ForeignKey(Mom_category, null=True, on_delete=models.CASCADE, related_name="momtask")  # noqa
    description = models.TextField(max_length=500)
    # date = models.DateField(widget=DateInput(format='%Y-%m-%d', attrs={'type': 'date'}), required=False)  # noqa
    date = models.DateField()
    # date_due = models.DateTimeField()

    def __str__(self):
        return self.title


# # PLACEHOLDER for Category table
# class Mom_category(models.Model):
#     id
#     user_id (fk)
#     work
#     home
#     private_time
#     other


# Contact Form table
class Mom_contact(models.Model):
    email = models.EmailField(max_length=50, null=False, blank=False)
    topic = models.CharField(max_length=50, null=False, blank=False)
    your_message = models.CharField(max_length=300)

    def __str__(self):
        return self.topic
