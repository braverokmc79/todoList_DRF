from rest_framework.views import APIView
from .serializers import TodoSerializer
from .models import Todo
from rest_framework.response import Response


#전체보기
class TodoListAPI(APIView):
    def get(self, request):
        todo = Todo.objects.all()
        serializer = TodoSerializer(todo, many=True)
        return Response(serializer.data) #일반 json 데이터 .data
    