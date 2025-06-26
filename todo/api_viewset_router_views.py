from rest_framework import viewsets
from .models import Todo
from .serializers import TodoSerializer

# ✅ ViewSet은 CRUD를 한 클래스에서 처리하며 Router와 함께 사용됨
# ✅ ViewSet 하나로 CRUD를 자동 처리 (GET, POST, PUT, DELETE)
class TodoViewSet(viewsets.ModelViewSet):
    #queryset = Todo.objects.all().order_by('-created_at')  
        
    def get_queryset(self):
        qs =Todo.objects.all().order_by('-created_at')
        return qs
    
    serializer_class = TodoSerializer
            
    
    