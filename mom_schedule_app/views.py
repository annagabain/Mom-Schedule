from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from .models import Mom_task

# for registering a new user
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages


def mom_home(request):
    return render(request, "index.html")


# change this to edit tasks page and create a separate base.html to extend
def index(request):
    mom_tasks = Mom_task.objects.all()
    return render(request, "base.html", {"mom_task_list": mom_tasks})


@require_http_methods(["POST"])
def add(request):
    title = request.POST["title"]
    mom_task = Mom_task(title=title)
    mom_task.save()
    return redirect("index")


def update(request, mom_task_id):
    mom_task = Mom_task.objects.get(id=mom_task_id)
    mom_task.complete = not mom_task.complete
    mom_task.save()
    return redirect("index")


def delete(request, mom_task_id):
    mom_task = Mom_task.objects.get(id=mom_task_id)
    mom_task.delete()
    return redirect("index")


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


def test_template(request):
    return render(request, "test.html")
