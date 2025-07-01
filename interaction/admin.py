from django.contrib import admin
from .models import Bookmark, Like, Comment, CommentLike


admin.site.register(Bookmark)
admin.site.register(Like)
admin.site.register(CommentLike)



@admin.register(Comment)  
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "user","todo", "content", "created_at")
    

    
"""
| 항목                              | 의미                                      |
| ------------------------------- | --------------------------------------- |
| `@admin.register(Comment)` | `Comment` 모델을 관리자 사이트에 등록               |
| `CommentAdmin`                  | 해당 모델을 어떻게 보여줄지 커스터마이징하는 클래스            |
| `list_display`                  | 목록 화면(리스트 페이지)*에서 어떤 필드를 보여줄지 지정 |


"""    