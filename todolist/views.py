from django.shortcuts import render, redirect, HttpResponse

from todolist.models import todos

# Create your views here.
def home(request):
    data = todos.objects.all()
    todo = {
    "id": data}
    return render(request,'home.html',todo)

def add(request):
    if request.method=='POST':
        title=request.POST.get('title')
        description=request.POST.get('description')
        add=todos(title=title,content=description)
        add.save()
    return redirect('/')


def delete(request,id):
    record = todos.objects.get(id = id)
    record.delete()
    return redirect('/')


def update(request,id):
    context={'id':id}
    if request.method=='POST':
        record = todos.objects.get(id = id)
        title=request.POST.get('title')
        description=request.POST.get('description')
        record.title=title
        record.content=description
        record.save()
        return redirect('/')
    return render(request,'update.html',context)




    
    