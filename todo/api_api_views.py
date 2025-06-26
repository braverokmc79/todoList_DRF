from rest_framework.views import APIView

from .serializers import TodoSerializer
from .models import Todo
from rest_framework.response import Response
from rest_framework import status
from django.http import *

"""
✅ 1. APIView (rest_framework.views.APIView)

📌 특징:
DRF에서 가장 기본이 되는 클래스 기반 뷰
Django의 View를 확장하여 request.data, Response, status 같은 DRF 기능을 제공
get(), post(), put() 등을 직접 구현해야 함
매우 유연함 — 복잡하거나 비표준 API에 적합

✅ 복잡한 비즈니스 로직 → APIView 사용
"""


# 전체 Todo 목록 조회
class TodoListAPI(APIView):
    def get(self, request):          
        todo = Todo.objects.all().order_by('-created_at') # 모든 Todo 객체를 가져온다              
        serializer = TodoSerializer(todo, many=True) # 시리얼라이저를 통해 데이터를 JSON 형식으로 변환
        return Response(serializer.data) # 변환된 데이터 응답


# Todo 생성 (POST 요청)
class TodoCreateAPI(APIView):
    def post(self, request):
        serializer = TodoSerializer(data=request.data) # 클라이언트로부터 전달된 데이터로 시리얼라이저 생성
        serializer.is_valid(raise_exception=True)      # 데이터 유효성 검사 (에러 발생 시 예외 처리)
        todo = serializer.save()  # 데이터 저장
        # 저장된 객체를 다시 시리얼라이징하여 응답
        return Response(TodoSerializer(todo).data, status=status.HTTP_201_CREATED)


# 특정 Todo 조회
class TodoRetrieveAPI(APIView):
    def get_object(self, pk):   # pk를 이용해 특정 Todo 객체 가져오기
        try:
            return Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            return None

    def get(self, request, pk):
        todo = self.get_object(pk)
        if todo is None:
            # 해당 Todo가 없을 경우 404 에러 응답
            return Response({"error": "해당 todo가 없습니다."}, status=status.HTTP_404_NOT_FOUND)

        # 있으면 시리얼라이징하여 응답
        serializer = TodoSerializer(todo)
        return Response(serializer.data, status=status.HTTP_200_OK)


# Todo 수정 (전체 수정: PUT / 부분 수정: PATCH)
class TodoUpdateAPI(APIView):
    # 전체 수정 (PUT)
    def put(self, request, pk):
        try:                        
            todo = Todo.objects.get(pk=pk) # 수정할 Todo 객체 가져오기
        except Todo.DoesNotExist:
            return Response({"error": "해당 Todo가 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)

        # 전체 필드를 기반으로 시리얼라이징 (덮어쓰기 방식)
        serializer = TodoSerializer(todo, data=request.data)
        serializer.is_valid(raise_exception=True)
        todo = serializer.save()
        return Response(TodoSerializer(todo).data)

    # 부분 수정 (PATCH)
    def patch(self, request, pk):
        try:
            todo = Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            return Response({"error": "해당 Todo가 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)

        # 부분 필드를 기반으로 시리얼라이징
        serializer = TodoSerializer(todo, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        todo = serializer.save()
        return Response(TodoSerializer(todo).data)


# Todo 삭제
class TodoDeleteAPI(APIView):
    def delete(self, request, pk):
        try:
            todo = Todo.objects.get(pk=pk)  # 삭제할 Todo 객체 가져오기
        except Todo.DoesNotExist:
            return Response({"error": "해당 Todo가 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)

        todo.delete()         # 객체 삭제
        # 삭제 성공 시 204 No Content 응답
        return Response(status=status.HTTP_204_NO_CONTENT)



#로그인  -> 제공해주는 형식 링크 DRF 제공 링크
#LogoutAPI -> 서버에 로그아웃 요청
#장고기본지원 -> 웹
#axios 방식 ->리액트 뷰, 언리얼엔진 , 유니티

from django.contrib.auth import logout
class CustomLogoutAPI(APIView):
    def post(self, request):
        logout(request)
        return Response({"message": "로그아웃 완료"}, status=status.HTTP_200_OK)