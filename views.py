from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import CustomUserCreationForm
@login_required
def index(request):
    tasks = Task.objects.filter(user=request.user)
    if request.method == "POST":
        new_task = request.POST.get("task")
        if new_task:
            Task.objects.create(user=request.user, title=new_task)
        return redirect("index")
    return render(request, "index.html", {"tasks": tasks})

from .forms import CustomUserCreationForm
from django.contrib.auth import login

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")
    else:
        form = CustomUserCreationForm()
    return render(request, "register.html", {"form": form})

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task

@login_required
def index(request):
    tasks = Task.objects.filter(user=request.user)

    if request.method == "POST":
        if "add_task" in request.POST:
            new_task = request.POST.get("task")
            if new_task:
                Task.objects.create(user=request.user, title=new_task)
            return redirect("index")

        if "delete_task" in request.POST:
            task_id = request.POST.get("delete_task")
            Task.objects.filter(id=task_id, user=request.user).delete()
            return redirect("index")

        if "complete_task" in request.POST:
            task_id = request.POST.get("complete_task")
            task = Task.objects.get(id=task_id, user=request.user)
            task.completed = not task.completed
            task.save()
            return redirect("index")

    return render(request, "index.html", {"tasks": tasks})
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from .ml_utils import suggest_daily_tasks   # import your ML function

@login_required
def dashboard(request):
    suggestions = suggest_daily_tasks(request.user)
    tasks = Task.objects.filter(user=request.user)

    if request.method == "POST":
        new_task = request.POST.get("task")
        if new_task:
            Task.objects.create(user=request.user, title=new_task)
        return redirect("dashboard")
    print("Rendering dashboard.html")
    return render(request, "dashboard.html", {
        "tasks": tasks,
        "suggestions": suggestions
    })
