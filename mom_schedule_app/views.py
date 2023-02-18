from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from .models import Mom_task, Mom_contact

from .forms import NewUserForm
# from .forms import NewUserForm, ContactForm

from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

# for restricting unautharized views
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User


def mom_home(request):
    return render(request, "index.html")


# only logged in users can see this page
@login_required(login_url='login')
def mom_task(request):
    mom_tasks = Mom_task.objects.filter(user=request.user)

    # keep this line for filtering the views!
    # mom_tasks = Mom_task.objects.filter(user=request.user, complete='False')
    # mom_tasks = Mom_task.objects.filter(complete='False').values()
    return render(request, "all_tasks.html", {"mom_task_list": mom_tasks})


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

    mom_task = Mom_task(title=title, description=description, date=date)
    mom_task.save()
    request.user.momtask.add(mom_task)
    return redirect("all_tasks")


@login_required(login_url='login')
def new(request):
    return render(request, 'new_task.html')


@login_required(login_url='login')
def edit(request, mom_task_id):
    mom_task = Mom_task.objects.get(id=mom_task_id)
    edit_task_form_fields = {
        "title": mom_task.title,
        "description": mom_task.description,
        "date": mom_task.date,
        "id": mom_task.id
    }
    return render(request, 'edit_task.html', context=edit_task_form_fields)


@login_required(login_url='login')
def update(request, mom_task_id):
    mom_task = Mom_task.objects.get(id=mom_task_id)
    mom_task.title = request.GET['title']
    mom_task.description = request.GET['description']
    mom_task.date = request.GET['date']
    mom_task.save()
    task_form_fields = {
        "alltasks": Mom_task.objects.all()
    }
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
