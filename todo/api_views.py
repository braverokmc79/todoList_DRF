import stat
from turtle import st
from rest_framework.views import APIView
from .serializers import TodoSerializer
from .models import Todo
from rest_framework.response import Response
from rest_framework import status

#전체보기
class TodoListAPI(APIView):
    def get(self, request):
        todo = Todo.objects.all()
        serializer = TodoSerializer(todo, many=True)
        return Response(serializer.data) #일반 json 데이터 .data
    
    


class TodoCreateAPI(APIView):
    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)      
        todo=serializer.save()
        return Response(TodoSerializer(todo).data, status=status.HTTP_201_CREATED)
    