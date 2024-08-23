from .common import FlowerPostSerializer
from comments.serializers.common import CommentSerializer
from categories.serializers.common import CategorySerializer
from jwt_auth.serializers.common import UserSerializer

class PopulatedFlowerPostSerializer(FlowerPostSerializer):
    comments = CommentSerializer(many=True)
    category = CategorySerializer()
    owner = UserSerializer()