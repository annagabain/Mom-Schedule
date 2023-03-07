from django.contrib import admin
from .models import Mom_task, Mom_contact, Task_Category
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Mom_task)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('title')
    search_fields = ['title', 'description']


admin.site.register(Mom_contact)
admin.site.register(Task_Category)
