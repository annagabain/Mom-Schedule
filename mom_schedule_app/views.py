from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from .models import Mom_task

# for registering a new user
from .forms import NewUserForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


def mom_home(request):
    return render(request, "index.html")


def mom_task(request):
    mom_tasks = Mom_task.objects.all()
    return render(request, "edit_task.html", {"mom_task_list": mom_tasks})


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
                return redirect("index")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})  # noqa


@require_http_methods(["POST"])
def add(request):
    title = request.POST["title"]
    mom_task = Mom_task(title=title)
    mom_task.save()
    return redirect("edit_task")


def update(request, mom_task_id):
    mom_task = Mom_task.objects.get(id=mom_task_id)
    mom_task.complete = not mom_task.complete
    mom_task.save()
    return redirect("edit_task")


def delete(request, mom_task_id):
    mom_task = Mom_task.objects.get(id=mom_task_id)
    mom_task.delete()
    return redirect("edit_task")
