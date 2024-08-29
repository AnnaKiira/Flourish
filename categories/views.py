from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Category
from utils.decorators import handle_exceptions
from .serializers.populated import PopulatedCategorySerializer

# Create your views here.
class CategoryListView(APIView):
    @handle_exceptions
    def get(self, request):
        categories = Category.objects.all()
        serialized_categories = PopulatedCategorySerializer(categories, many=True)
        return Response(serialized_categories.data)