from .common import FlowerPostSerializer
from comments.serializers.common import CommentSerializer
from categories.serializers.common import CategorySerializer

class PopulatedFlowerPostSerializer(FlowerPostSerializer):
    comments = CommentSerializer(many=True)
    category = CategorySerializer()