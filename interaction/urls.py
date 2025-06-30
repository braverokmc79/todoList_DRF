from django.urls import path ,include

from python.bookproject.books.models import Book
from .api_viewset_router_views import LikeViewSet , BookmarkViewSet , CommentViewSet

#ViewSets 설정
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register("" , LikeViewSet, basename="like")
router.register("" , BookmarkViewSet, basename="bookmarks")
router.register("" , CommentViewSet, basename="comments")


app_name="interaction"


urlpatterns = [
  path("viewsets/", include(router.urls)),     
]    



 


