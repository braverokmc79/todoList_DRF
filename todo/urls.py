from django.urls import path
from . import views
from . import api_views
from .generic_api_view import *

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
  #http://127.0.0.1:8000/todo/api/create/
  #http://127.0.0.1:8000/todo/retrieve/1/
  #http://127.0.0.1:8000/todo/api/update/1
  #http://127.0.0.1:8000/todo/api/delete/1
  
  # apiViews
  path("api/list/", api_views.TodoListAPI.as_view(), name="todo_api_list"),  
  path("api/create/", api_views.TodoCreateAPI.as_view(), name="todo_api_create"),  
  path("api/retrieve/<int:pk>/", api_views.TodoRetrieveAPI.as_view(), name="todo_api_retrieve"),
  path("api/update/<int:pk>/", api_views.TodoUpdateAPI.as_view(), name="todo_api_update"),
  path("api/delete/<int:pk>/", api_views.TodoDeleteAPI.as_view(), name="todo_api_delete"),
  
  
  #   # apiViews
  # path("generics/list/", api_views.TodoListAPI.as_view(), name="todo_api_list"),  
  # path("generics/create/", api_views.TodoCreateAPI.as_view(), name="todo_api_create"),  
  # path("generics/retrieve/<int:pk>/", api_views.TodoRetrieveAPI.as_view(), name="todo_api_retrieve"),
  # path("generics/update/<int:pk>/", api_views.TodoUpdateAPI.as_view(), name="todo_api_update"),
  # path("generics/delete/<int:pk>/", api_views.TodoDeleteAPI.as_view(), name="todo_api_delete"),
  

  
  #GenericAPIView
  path("generics/list/", TodoGenericsListAPI.as_view(), name="todo_generics_list"),
  path("generics/create/", TodoGenericsCreateAPI.as_view(), name="todo_generics_create"),
  path("generics/retrieve/<int:pk>/", TodoGenericsRetrieveAPI.as_view(), name="todo_generics_retrieve"),
  path("generics/update/<int:pk>/", TodoGenericsUpdateAPI.as_view(), name="todo_generics_update"),  
    # 단독 삭제
  path("generics/delete/<int:pk>/", TodoGenericsDeleteAPI.as_view(), name="todo_generics_delete"),
  # List + Create
  path("generics/list-create/", TodoGenericsListCreateAPI.as_view(), name="todo_generics_list_create"),
  # Retrieve + Update + Delete (RUD)
  path("generics/rud/<int:pk>/", TodoGenericsRetrieveUpdateDeleteAPI.as_view(), name="todo_generics_rud"),

]


