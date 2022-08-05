from unicodedata import name
from django.shortcuts import redirect, render
from .models import Task
from django.utils import timezone

# Create your views here.
def home(request):
    my_task = Task.objects.all()
    '''Render users to homepage'''
    return render(request,'users.html',{'my_task':my_task})

def edit(request):
    '''Render the edit page'''
    return render(request,'edit.html')

def index(request):
    '''Render the index page'''
    return render(request,'index.html')

def log(request):
    '''Render the login page'''
    return render(request,'log.html')

def profile(request):
    '''Render the profile page'''
    return render(request,'profile.html')
    
def sign(request):
    '''Render the sign up page'''
    return render(request,'sign.html')

def add_task(request):
    '''Adds task to the task table/homepage'''    
    if request.method == 'POST':       
        task_passed = request.POST.get('task')
        if task_passed:                 #To make sure we dont add an empty task
            new_task = Task()
            new_task.name = task_passed
            new_task.save()
    return redirect('home')

def delete(request):
    '''Deletes task from the task table/homepage'''
    deleted_item = request.GET.get('task_to_delete')
    del_item = Task.objects.get(id = deleted_item)
    del_item.delete()
    return redirect('home')

def update(request):
    '''Editing task from the task table/homepage'''
    if request.method == 'POST':
        Edited_item = request.POST.get('task_to_edit')
        print(Edited_item)
        if Edited_item:
            current_date = timezone.now()
            edit_item = Task.objects.get(name =Edited_item)
            edit_item.name = Edited_item
            edit_item.date_created = current_date
            edit_item.save()
        return redirect('home')

    else:
        return redirect('home')


