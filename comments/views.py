from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Comment
from .serializers.common import CommentSerializer
from utils.decorators import handle_exceptions

# Create your views here.
class CommentCreateView(APIView):
    #Create Comment /comments
    @handle_exceptions
    def post(self, request):
        comment_to_create = CommentSerializer(data=request.data)
        if comment_to_create.is_valid():
            comment_to_create.save()
            return Response(comment_to_create.data, 201)
        return Response(comment_to_create.errors, 400)