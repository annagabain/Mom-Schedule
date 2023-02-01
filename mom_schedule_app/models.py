from django.db import models


class Mom_task(models.Model):
    # Database columns are here!!
    title = models.CharField(max_length=350)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title
