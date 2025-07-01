from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets
from python.todoList_DRF.todo.serializers import TodoSerializer
from todo.models import Todo
from .serializers import LikeSerializer , BookmarkSerializer, CommentSerializer, CommentLikeSerializer
from .models import Like, Bookmark, Comment, CommentLike
from rest_framework import permissions
from rest_framework.decorators import action



class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]  # ✅ 인증된 사용자만 접근 가능

    @action(detail=True, methods=['post'])
    def toggle(self, request, pk=None):
        todo = Todo.objects.get(pk=pk)  # 해당 Todo 가져오기
        user = request.user             # 현재 로그인한 사용자

        # Like 객체가 있으면 가져오고 없으면 새로 생성
        like, created = Like.objects.get_or_create(user=user, todo=todo)

        # 현재 상태 반전
        like.is_like = not like.is_like
        like.save()

        # 결과로 Todo 정보 반환
        serialize = TodoSerializer(todo, context={'request': request})
        return Response(serialize.data)


"""
    @action은 이 메서드(toggle)를 하나의 API 엔드포인트로 등록해줍니다.
    detail=True이므로, 이 엔드포인트는 URL에 pk가 필요한 detail route로 작동합니다.
    예: /like/3/toggle/ → pk=3인 대상에 대해 동작
    methods=['post']는 POST 요청만 허용한다는 뜻입니다.
"""

        
        

class BookmarkViewSet(viewsets.ModelViewSet): # 북마크 기능을 위한 ViewSet
    queryset = Bookmark.objects.all() 
    serializer_class = BookmarkSerializer 
    permission_classes = [permissions.IsAuthenticated] 

    @action(detail=True, methods=["post"]) 
    def toggle(self, request, pk=None): 
        todo = Todo.objects.get(pk=pk) 
        user = request.user

        bookmark, created = Bookmark.objects.get_or_create(todo=todo, user=user) 
        bookmark.is_marked = not bookmark.is_marked 
        bookmark.save() 

        serializer = TodoSerializer(todo, context={"request": request}) 
        return Response(serializer.data) 




class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        todo_id = self.request.query_params.get("todo_pk") #쿼리스트링 ?todo_pk=1을 받아서 해당 Todo에 연결된 댓글만 조회
        return Comment.objects.filter(todo_id=todo_id).order_by("-created_at") #최신순 정렬 (-created_at)

    def perform_create(self, serializer):
        todo_id = self.request.data.get("todo_pk")  #댓글 생성 시 todo_pk를 POST body에서 받음
        todo = Todo.objects.get(pk=todo_id)  #해당 Todo 객체를 조회해서 댓글에 연결
        serializer.save(user=self.request.user, todo=todo)   #작성자는 현재 로그인된 사용자 (request.user)
    
    
    
    
    
class CommentLikeViewSet(viewsets.ModelViewSet):
    queryset = CommentLike.objects.all()
    serializer_class = CommentLikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['post'])  # /commentlikes/{pk}/toggle/
    def toggle(self, request, pk=None):
        comment = get_object_or_404(Comment, pk=pk)
        user = request.user
        like, created = CommentLike.objects.get_or_create(comment=comment, user=user)
        like.is_like = not like.is_like
        like.save()
        return Response({
            "is_liked": like.is_like,
            "like_count": CommentLike.objects.filter(comment=comment, is_like=True).count()
        })
    




    


    