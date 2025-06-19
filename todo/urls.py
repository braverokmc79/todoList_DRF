from django.urls import path
from . import views
from . import api_views

app_name = "todo"  # 네임스페이스 지정
  
urlpatterns = [
  #path("list/", views.todo_list, name="todo_list"),
  
  #템플릿 Views
  path("list/", views.TodoListView.as_view(), name="todo_list"),
 
  # apiViews
  path("api/list/", api_views.TodoListAPI.as_view(), name="todo_api_list"),
  
  
]


