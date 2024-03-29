# Generated by Django 3.2.17 on 2023-02-24 13:57

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mom_schedule_app', '0012_mom_task_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mom_task',
            options={'ordering': ['date']},
        ),
        migrations.AddField(
            model_name='mom_task',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),  # noqa
        ),
    ]
