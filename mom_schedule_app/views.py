from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from .models import *
# from .models import Mom_task, Mom_contact, Task_Category
from django.core import serializers
# from .forms import NewUserForm
# from .forms import NewUserForm, ContactForm
from .forms import *

from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

# for restricting unautharized views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views import generic
from datetime import datetime
from django.views import generic
from django.utils.safestring import mark_safe
from .utils import Calendar


def mom_home(request):
    return render(request, "index.html")


# only logged in users can see this page
@login_required(login_url='login')
def mom_task(request):
    mom_tasks = Mom_task.objects.filter(user=request.user)
    task_category_context = Task_Category.objects.all()
    print('=========================================')
    print('all tasks - CATEGORY INDEX', task_category_context)
    print('=========================================')
    return render(request, "all_tasks.html", {"mom_task_list": mom_tasks, 'Task_Category': task_category_context})  # noqa


@login_required(login_url='login')
def all_tasks_complete(request):
    task_category_context = Task_Category.objects.all()
    mom_tasks_complete = Mom_task.objects.filter(user=request.user, complete='True')  # noqa
    return render(request, "all_tasks_complete.html", {"mom_task_list": mom_tasks_complete, "Task_Category": task_category_context})  # noqa


@login_required(login_url='login')
def all_tasks_hide_complete(request):
    task_category_context = Task_Category.objects.all()
    all_tasks_hide_complete = Mom_task.objects.filter(user=request.user, complete='False')  # noqa
    return render(request, "all_tasks_hide_complete.html", {"mom_task_list": all_tasks_hide_complete, "Task_Category": task_category_context})  # noqa


@login_required(login_url='login')
def all_tasks_filter_date(request):
    task_category_context = Task_Category.objects.all()
    all_tasks_filter_date = Mom_task.objects.filter(user=request.user).order_by('date').values()  # noqa
    return render(request, "all_tasks_filter_date.html", {"mom_task_list": all_tasks_filter_date, "Task_Category": task_category_context})  # noqa


@login_required(login_url='login')
def all_tasks_filter_category(request):
    category = request.POST["category"]
    task_category_context = Task_Category.objects.all()
    all_tasks_filter_category = Mom_task.objects.filter(user=request.user).filter(category=int(category))  # noqa

    return render(request, "all_tasks_filter_category.html", {"mom_task_list": all_tasks_filter_category, "Task_Category": task_category_context})  # noqa


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("index")
        messages.error(request, "Unsuccessful registration. Invalid information.")  # noqa
    form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form": form})  # noqa


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("all_tasks")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})  # noqa


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("index")


def mom_contact(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        topic = request.POST.get('topic')
        your_message = request.POST.get('your_message')
        Mom_contact.objects.create(email=email, topic=topic, your_message=your_message)  # noqa
        messages.info(request, "We received your message and will respond soon.")  # noqa

        return redirect('index')
    return render(request, 'contact.html')


@login_required(login_url='login')
@require_http_methods(["POST"])
def add(request):
    title = request.POST["title"]
    description = request.POST["description"]
    date = request.POST["date"]
    category = request.POST["category"]

    category_id = None
    for cat in Task_Category.objects.all():
        # print('cat.name', cat.name)
        # print('cat.pk', cat.pk)
        if cat.pk == int(category):
            category_id = cat

    # print('=========================================')
    # print('add - CATEGORY INDEX', category)
    # print('=========================================')

    mom_task = Mom_task(title=title, category=category_id, description=description, date=date)  # noqa
    mom_task.save()
    request.user.momtask.add(mom_task)
    return redirect("all_tasks")


@login_required(login_url='login')
def new(request):
    task_category_context = Task_Category.objects.all()
    mom_task__context = Mom_task.objects.filter(user=request.user)
    return render(request, 'new_task.html', {'Task_Category': task_category_context, 'Mom_task': mom_task__context})  # noqa


@login_required(login_url='login')
def edit(request, mom_task_id):
    task_category_context = Task_Category.objects.all()
    mom_task = Mom_task.objects.get(id=mom_task_id)

    edit_task_form_fields = {
        "title": mom_task.title,
        "Task_Category": task_category_context,
        "description": mom_task.description,
        # <!-- TRY TO PREPOPULATE -->
        "category": mom_task.category,
        "date": mom_task.date.strftime("%Y-%m-%d"),
        "id": mom_task.id
    }
    return render(request, 'edit_task.html', context=edit_task_form_fields)  # noqa


@login_required(login_url='login')
def update(request, mom_task_id):
    mom_task = Mom_task.objects.get(id=mom_task_id)

    mom_task.title = request.GET['title']
    mom_task.description = request.GET['description']
    mom_task.date = request.GET['date']

    selected_category_id = request.GET["category"]

    category_find = None
    for cat in Task_Category.objects.all():
        # print('cat.name', cat.name)
        # print('cat.pk', cat.pk)
        if cat.pk == int(selected_category_id):
            category_find = cat
    # print('category_id', category_find)

    mom_task.category = category_find

    mom_task.save()
    return redirect("all_tasks")


def toggle_complete(request, mom_task_id):
    mom_task = Mom_task.objects.get(id=mom_task_id)
    mom_task.complete = not mom_task.complete
    mom_task.save()
    return redirect("all_tasks")


@login_required(login_url='login')
def delete(request, mom_task_id):
    mom_task = Mom_task.objects.get(id=mom_task_id)

    if request.method == 'POST':
        mom_task.delete()
        return redirect("all_tasks")

    return render(request, 'delete_task.html', {'mom_task': mom_task})


def calendar(request):
    return render(request, 'calendar.html')


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split("-"))
        return date(year, month, day=1)
    return datetime.today()


# class CalendarView(LoginRequiredMixin, generic.ListView):
class CalendarView(generic.ListView):

    # login_url = "accounts:signin"
    model = Mom_task
    template_name = "calendar.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get("month", None))
        # d = get_date(self.request.GET.get('day', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context["calendar"] = mark_safe(html_cal)
        # context["prev_month"] = prev_month(d)
        # context["next_month"] = next_month(d)
        return context


# def get_date(req_day):
#     if req_day:
#         year, month = (int(x) for x in req_day.split('-'))
#         return date(year, month, day=1)
#     return datetime.date.today()
