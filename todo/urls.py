from django.urls import path
from . import views
from . import api_views

app_name = "todo"  # 네임스페이스 지정
  
urlpatterns = [
  #path("list/", views.todo_list, name="todo_List"),
  
  #http://127.0.0.1:8000/todo/list/
  #템플릿 Views
  path("list/", views.TodoListViews.as_view(), name="todo_List"),
  #http://127.0.0.1:8000/todo/create/
  path("create/", views.TodoCreateViews.as_view(), name="todo_Create"),
  #http://127.0.0.1:8000/todo/detail/1
  path("detail/<int:pk>/", views.TodoDetailViews.as_view(), name="todo_Detail"),
  #http://127.0.0.1:8000/todo/update/1
  path("update/<int:pk>/", views.TodoUpdateViews.as_view(), name="todo_Update"),

 
  #http://127.0.0.1:8000/todo/api/list/
  # apiViews
  path("api/list/", api_views.TodoListAPI.as_view(), name="todo_api_list"),
  #http://127.0.0.1:8000/todo/api/create/
  path("api/create/", api_views.TodoCreateAPI.as_view(), name="todo_api_create"),  
  #http://127.0.0.1:8000/todo/retrieve/1/
  path("api/retrieve/<int:pk>/", api_views.TodoRetrieveAPI.as_view(), name="todo_api_retrieve"),
  #http://127.0.0.1:8000/todo/api/update/1
  path("api/update/<int:pk>/", api_views.TodoUpdateAPI.as_view(), name="todo_api_update"),
  #http://127.0.0.1:8000/todo/api/delete/1
  path("api/delete/<int:pk>/", api_views.TodoDeleteAPI.as_view(), name="todo_api_delete"),
  

  
]


