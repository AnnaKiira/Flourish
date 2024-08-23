from .common import CategorySerializer
from flowerposts.serializers.common import FlowerPostSerializer

class PopulatedCategorySerializer(CategorySerializer):
    flowerposts = FlowerPostSerializer(many=True)