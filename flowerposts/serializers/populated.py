from .common import FlowerPostSerializer
from comments.serializers.common import CommentSerializer

class PopulatedFlowerPostSerializer(FlowerPostSerializer):
    comments = CommentSerializer(many=True)