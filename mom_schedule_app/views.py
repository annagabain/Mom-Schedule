from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from .models import Mom_task


def index(request):
    mom_tasks = Mom_task.objects.all()
    # return render(request, "base.html")
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
