from django.urls import path
from . import views
from . import api_views

app_name = "todo"  # 네임스페이스 지정
  
urlpatterns = [
  #path("list/", views.todo_list, name="todo_list"),
  
  #http://127.0.0.1:8000/todo/list/
  #템플릿 Views
  path("list/", views.TodoListView.as_view(), name="todo_list"),
  #http://127.0.0.1:8000/todo/create/
  path("create/", views.TodoCreateView.as_view(), name="todo_create"),
  
 
 
 
  #http://127.0.0.1:8000/todo/api/list/
  # apiViews
  path("api/list/", api_views.TodoListAPI.as_view(), name="todo_api_list"),
  #http://127.0.0.1:8000/todo/api/create/
  path("api/create/", api_views.TodoCreateAPI.as_view(), name="todo_api_create"),
  
]


