from rest_framework import serializers
from .models import Like, Bookmark, Comment, CommentLike
from django.contrib.auth.models import User
from todo.models import Todo


# 👍 좋아요 직렬화
class LikeSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)  # 확인용
    todo_name = serializers.CharField(source="todo.name", read_only=True)     # 확인용

    class Meta:
        model = Like
        fields = ["id", "todo", "todo_name", "user", "username", "is_like"]
        read_only_fields = ["user", "username", "todo_name"]
        
        


# ⭐ 북마크 직렬화
class BookmarkSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)   # 출력 전용
    todo_name = serializers.CharField(source="todo.name", read_only=True)      # 출력 전용

    class Meta:
        model = Bookmark
        fields = ["id", "todo", "todo_name", "user", "username", "is_marked"]
        read_only_fields = ["user", "username", "todo_name"]
        
        
        

# 💬 댓글 직렬화
class CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)   
    todo_name = serializers.CharField(source="todo.name", read_only=True)      
    like_count = serializers.SerializerMethodField()                            # 좋아요 수 계산용

    class Meta:
        model = Comment
        fields = [
            "id", "todo", "todo_name",
            "user", "username",
            "content", "created_at",
            "like_count",
        ]
        read_only_fields = ["todo", "user", "created_at"]

    def get_like_count(self, obj):
        return obj.likes.count()

    def get_is_liked(self, obj):
        request = self.context.get("request")
        if request and request.user.is_authenticated:
            return obj.likes.filter(id=request.user.id).exists()
        return False


# ❤️ 댓글 좋아요 직렬화
class CommentLikeSerializer(serializers.ModelSerializer):
    username =serializers.CharField(source='user.username', read_only=True)
    
    comment_content = serializers.CharField(source='comment.content', read_only=True)
    

    class Meta:
        model = Comment
        fields = ['id', 'user', 'username' ,   'comment',  'comment_content',  'is_liked']
        read_only_fields = ['user']
