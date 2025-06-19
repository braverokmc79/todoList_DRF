from django.shortcuts import render
from .models import Todo
from django.views.generic import ListView
from django.urls import reverse_lazy


def todo_list(request):  #테스트용
    todo =Todo.objects.all()
    return render(request, 'todo/todo_list.html', {"todos": todo}) 


class TodoListView(ListView): #제너릭뷰  
    model = Todo
    template_name = "todo/todo.html"
    context_object_name = "todos"
    ordering = ["-created_at"]  
    #success_url = reverse_lazy("todo_list")
    
    
    
    
