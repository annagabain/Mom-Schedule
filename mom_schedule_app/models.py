from django.db import models
from django.contrib.auth.models import User


# Database columns are here!!
# Task table
class Mom_task(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="momtask")  # noqa
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=300)
    complete = models.BooleanField(null=False, blank=False, default=False)
    # date_due
    # starred
    # category

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
