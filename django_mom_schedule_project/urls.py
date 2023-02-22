"""django_mom_schedule_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from mom_schedule_app import views

app_name = 'mom_schedule_app'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.mom_home, name='index'),
    path('register', views.register_request, name='register'),
    path('login', views.login_request, name='login'),
    path('logout', views.logout_request, name='logout'),
    path('contact', views.mom_contact, name='mom_contact'),
    path('all_tasks', views.mom_task, name='all_tasks'),
    path('add', views.add, name='add'),
    path('new_task', views.new, name='new_task'),
    path('edit/<int:mom_task_id>/', views.edit, name='edit'),
    path('delete/<int:mom_task_id>/', views.delete, name='delete'),
    path('update/<int:mom_task_id>/', views.update, name='update'),
    path('toggle_complete/<int:mom_task_id>/', views.toggle_complete, name='toggle_complete'),  # noqa
    path('calendar', views.calendar, name='calendar'),
    path('all_tasks_complete', views.all_tasks_complete, name='all_tasks_complete'),  # noqa
    path('all_tasks_hide_complete', views.all_tasks_hide_complete, name='all_tasks_hide_complete'),  # noqa
    path('all_tasks_filter_date', views.all_tasks_filter_date, name='all_tasks_filter_date'),  # noqa
]
