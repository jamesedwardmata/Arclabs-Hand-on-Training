from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response


from .serializers import PostSerializer
from .serializers import MockSerializer
from .models import Post
from .models import mock_data
  
class TestAppView(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        qs = Post.objects.all()
        serializer = PostSerializer(qs, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializers = PostSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)

class DocsView(APIView):
    def get(self, request, *args, **kwargs):
        querys = mock_data.objects.all()
        serializer = MockSerializer(querys, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializers = MockSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)
    






