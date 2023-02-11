from django.db import models
from django.contrib.auth.models import User


class Mom_task(models.Model):
    # Database columns are here!!
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="momtask")  # noqa
    title = models.CharField(max_length=200)
    # user_id
    # heading
    # date_due
    # starred
    # category
    description = models.CharField(max_length=300)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title


# PLACEHOLDER for User table
# class Mom_user(models.Model):
    # user_id
#     user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
#     username = models.CharField(max_length=10, null=True)
#     email = models.EmailField()
# #     password
#     is_admin = = models.BooleanField(default=False)
#     created_at
#     updated_at

    # def __str__(self):
    #     return self.username


# # PLACEHOLDER for Category table
# class Mom_category(models.Model):
#     id
#     user_id (fk)
#     work
#     home
#     private_time
#     other
