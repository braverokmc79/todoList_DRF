from django.db import models
from django.contrib.auth.models import User
from todo.models import Todo


# 👍 좋아요 모델
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)

    is_like = models.BooleanField(default=True)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'todo'], name='unique_user_todo_like')
        ]

    def __str__(self):
        return f"{self.user.username} ❤️ {self.todo.name}"


# ⭐ 북마크 모델
class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)

    is_marked = models.BooleanField(default=True)
    
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'todo'], name='unique_user_todo_bookmark')
        ]

    def __str__(self):
        return f"{self.user.username} 📌 {self.todo.name}"


# 💬 댓글 모델
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    # 댓글 좋아요: 중간 테이블로 연결 ,  related_name='liked_comments':  역참조 시 사용할 이름을 지정
    likes = models.ManyToManyField(User, through='CommentLike', related_name='liked_comments', blank=True)

    def __str__(self):
        return f"{self.user.username} 💬 {self.content[:20]}"

"""
✅ 2. through='CommentLike'
Django가 자동으로 M2M 중간 테이블을 생성하는 대신,
CommentLike라는 사용자 정의 중간 테이블을 사용하겠다는 의미입니다.
이 중간 테이블에 liked_at 같은 추가 필드를 넣을 수 있습니다.
"""



# ❤️ 댓글 좋아요 모델
class CommentLike(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    liked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'comment'], name='unique_user_comment_like')
        ]

    def __str__(self):
        return f"{self.user.username} 👍 댓글 ID: {self.comment.id}"
