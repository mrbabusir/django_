from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse 
from django.views.decorators.http import require_POST
from .models import Todolist

# Create your views here.
def index(request):
    return render(request,'index.html')
def contact_us(request):
    return HttpResponse('Contact Us page')
def about_us(request):
    return HttpResponse('About Us page')
def home(request):
    person = [
        {"name":"Ram",
         "age" : 67
         },
        {"name":"Shyam",
         "age" : 25
         },
        {"name":"Hari",
         "age" : 51
         },
        {"name":"Shiva",
         "age" : 12
         },
        {"name":"Jack",
         "age" :15
         },
        {"name":"Johns",
         "age" : 35}
        
    ]
    context = {
        "name" : "Home Page",
        "age"  : 25,
        "persons" : person
    }
    return render(request,'home.html',context)
def list(request):
    
    obj = Todolist.objects.all()
    tasks = obj.all()
    all = obj.all().count()
    completed = obj.filter(is_completed=True).count()
    pending = obj.filter(is_completed=False).count()

    context = {
        "tasks" : tasks,
        "all" : all,
        "completed" : completed,
        "pending" : pending,
    }
    return render(request,'task.html',context)
def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        if title == '' or description == '':
            context ={
                'error':'Please fill all the fields'
                }
            return render(request,'create.html',context)
        Todolist.objects.create(title = title, description = description)
        return redirect('/task/')
        
    return render(request,'create.html')
def mark(request, pk):
    task = Todolist.objects.get(pk = pk)
    task.is_completed = True    
    task.save()
    return redirect('/task')

def edit(request, pk):
    task = Todolist.objects.get(pk=pk)
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.save()
        return redirect('/task')
    context = {
        'task': task,
    }
    return render(request, 'edit.html', context)
def delete(request, pk):
    task = Todolist.objects.filter( pk =pk)
    task.delete()
    return redirect('/task')