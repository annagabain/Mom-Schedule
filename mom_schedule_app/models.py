from django.db import models


class Mom_task(models.Model):
    # Database columns are here!!
    title = models.CharField(max_length=200)
    # user
    # heading
    # date_due
    # starred
    # category
    description = models.CharField(max_length=300)
    complete = models.BooleanField(default=False)

    # def __str__(self):
    #     return self.title

# PLACEHOLDER for Category table
# class Mom_category(models.Model):
#     id
#     user_id
#     work
#     home
#     private_time
#     other
