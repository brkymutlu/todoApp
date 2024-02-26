from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import *

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        # todo = Todo.objects.all()
        todo = Todo.objects.filter(user = request.user)
        if request.method == 'POST': # HTML den admin tarafına veri göndereceğimiz zaman bu methodu kullanırız 
            #! HTML tarafında ilgili yapı formun içinde ve type submit olmalıdır
            form = TodoForm(request.POST)
            if form.is_valid():
                userTodo = form.save(commit=False)
                userTodo.user = request.user
                userTodo.save()
                return redirect('index') 
        
        else:

            form = TodoForm()
        context = {
            'todo':todo,
            'form':form,
        }
        return render (request,'index.html',context)
    else:
        return render (request,'index.html')

def todoDetay(request,d_slug):
    todo = get_object_or_404(Todo, slug = d_slug)
    context = {
        'todo':todo,
    }
    return render (request,'todoDetay.html',context)

def sil(request):
    if request.method == 'POST':
        todoId = request.POST['sil']
        sil = Todo.objects.get(id = todoId) # İlk değer veritabanından alır ve kendi belirlediğimiz id ile eşleşirse silme işlemine devam eder 
        sil.delete()
        return redirect('index')