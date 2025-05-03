from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.db.models import Case, When, Value, IntegerField

# Create your views here.

@login_required
def home(request):
    tasks = Task.objects.filter(user=request.user)
    sort = request.GET.get('sort')
    sort_list = ['start_date', 'due_date', 'task_urgency']
    if sort == 'task_urgency':
        tasks = tasks.annotate(
            urgency_order=Case(
                When(task_urgency='CR', then=Value(1)),
                When(task_urgency='HI', then=Value(2)),
                When(task_urgency='ME', then=Value(3)),
                When(task_urgency='LO', then=Value(4)),
                default=Value(5),
                output_field=IntegerField()
            )
        ).order_by('urgency_order')
    elif sort in sort_list:
        tasks = tasks.order_by(sort)
    else:
        tasks = tasks.order_by('due_date')
    now = timezone.now().date()
    task_data = []
    for task in tasks:
        if task.due_date:
            due_date = task.due_date.date() if hasattr(task.due_date, 'date') else task.due_date
            days_left = (due_date - now).days
        else:
            days_left = None
        task_data.append({
            'task': task,
            'days_left': days_left,
            'abs_days_left': abs(days_left) if days_left is not None else None
        })
    return render(request, 'tasks/home.html', {'tasks': tasks, 'sort': sort, 'task_data': task_data})

@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('home')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})

@login_required
def edit_task(request, id):
    task = Task.objects.get(id=id)
    if task.user != request.user:
        return redirect('home')
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})

@login_required
def delete_task(request, id):
    task = Task.objects.get(id=id)
    if task.user == request.user:
        task.delete()
    return redirect('home')

@login_required
def complete_task(request, id):
    task = Task.objects.get(id=id)
    if task.user == request.user:
        task.completed = True
        task.save()
    return redirect('home')

@login_required
def dashboard(request):
    tasks = Task.objects.filter(user=request.user)
    total = tasks.count()
    completed = tasks.filter(completed=True).count()
    pending = total - completed
    homework = tasks.filter(task_type='HW').count()
    exams = tasks.filter(task_type='EX').count()
    projects = tasks.filter(task_type='PR').count()

    return render(request, 'tasks/dashboard.html', {
        'total': total,
        'completed': completed,
        'pending': pending,
        'homework': homework,
        'exams': exams,
        'projects': projects,
    })