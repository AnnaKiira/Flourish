from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Comment
from .serializers.common import CommentSerializer
from rest_framework.permissions import IsAuthenticated
from utils.decorators import handle_exceptions

# Create your views here.
class CommentCreateView(APIView):
    permission_classes = [IsAuthenticated]
    #Create Comment /comments
    @handle_exceptions
    def post(self, request):
        request.data['owner'] = request.user.id
        comment_to_create = CommentSerializer(data=request.data)
        if comment_to_create.is_valid():
            comment_to_create.save()
            return Response(comment_to_create.data, 201)
        return Response(comment_to_create.errors, 400)
    

class CommentDestroyView(APIView):
    #Delete comment /comments/:pk/
    @handle_exceptions
    def delete(self, request, pk):
        comment_to_delete = Comment.objects.get(pk=pk)
        comment_to_delete.delete()
        return Response(status=204)