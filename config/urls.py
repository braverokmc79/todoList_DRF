from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from django.shortcuts import redirect


urlpatterns = [
    path('admin/', admin.site.urls),
    path("todo/", include("todo.urls")),
    path("", lambda request:redirect("todo:todo_List") ),
]



