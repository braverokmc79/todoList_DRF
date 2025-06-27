from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from django.shortcuts import redirect

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path("todo/", include("todo.urls")),
    path("", lambda request:redirect("todo:todo_List") ),
    path("api-auth/", include("rest_framework.urls")  , name="login"),
    path("accounts/", include("django.contrib.auth.urls")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



