from rest_framework import serializers
from jwt_auth.models import User
from flowerposts.serializers.populated import PopulatedFlowerPostSerializer

class UserProfileSerializer(serializers.ModelSerializer):
    flowerposts_created = PopulatedFlowerPostSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'flowerposts_created']