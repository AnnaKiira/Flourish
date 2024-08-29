from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers.common import UserSerializer
from utils.decorators import handle_exceptions
from rest_framework_simplejwt.tokens import RefreshToken
User = get_user_model()

# Create your views here.
#Sign up view for creating a user
class SignUpView(APIView):
    @handle_exceptions
    def post(self, request):
        user_to_create = UserSerializer(data=request.data)
        if user_to_create.is_valid():
            user = user_to_create.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'message': 'Sign Up Successful',
                'access': str(refresh.access_token),
                'refresh': str(refresh)
            }, status=201)
        return Response(user_to_create.errors, 400)