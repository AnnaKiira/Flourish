#from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers.common import UserProfileSerializer

# Create your views here.
class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serialized_user = UserProfileSerializer(request.user)
        return Response(serialized_user.data)