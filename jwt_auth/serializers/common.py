from rest_framework import serializers
from django.contrib.auth import get_user_model, password_validation
User = get_user_model()
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)

    def validate(self, data):
        password = data.pop('password')
        password_confirmation = data.pop('password_confirmation')
        if password != password_confirmation:
            raise serializers.ValidationError({'password_confirmation': 'Passwords Do Not Match'})
        password_validation.validate_password(password=password)
        data['password'] = make_password(password)
        return data
    
    class Meta: 
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name', 'password', 'password_confirmation')