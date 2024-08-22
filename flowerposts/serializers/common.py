from rest_framework.serializers import ModelSerializer
from ..models import FlowerPost

class FlowerPostSerializer(ModelSerializer):
    class Meta:
        model = FlowerPost
        fields = '__all__'