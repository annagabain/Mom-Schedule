from django.db import models
from django.contrib.auth.models import User


class Mom_task(models.Model):
    # Database columns are here!!
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="momtask")  # noqa
    title = models.CharField(max_length=50, null=False, blank=False)
    # date_due
    # starred
    # category
    description = models.CharField(max_length=300)
    complete = models.BooleanField(null=False, blank=False, default=False)

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


# # PLACEHOLDER for Contact Form table
class Mom_contact(models.Model):
    email = models.EmailField(max_length=254)
    topic = models.CharField(max_length=50, null=False, blank=False)
    your_message = models.CharField(max_length=300)
