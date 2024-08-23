from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FlowerPost
from .serializers.common import FlowerPostSerializer
from utils.decorators import handle_exceptions
from flowerposts.serializers.populated import PopulatedFlowerPostSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
#from rest_framework.exceptions import PermissionDenied
from utils.permissions import IsOwnerOrReadOnly

# Create your views here.
class FlowerPostListCreateView(APIView):
    permission_classes = [IsAuthenticated]
    #INDEX Route
    @handle_exceptions
    def get(self, request):
        flowerposts = FlowerPost.objects.all()
        serialized_flowerposts = FlowerPostSerializer(flowerposts, many=True)
        #print(serialized_flowerposts.data)
        return Response(serialized_flowerposts.data)
    
    
    #CREATE Route
    @handle_exceptions
    def post(self, request):
        request.data['owner'] = request.user.id
        flowerpost_to_create = FlowerPostSerializer(data=request.data)
        if flowerpost_to_create.is_valid():
            #data is valid
            flowerpost_to_create.save()
            return Response(flowerpost_to_create.data, 201)
            
        #error occurred during validation
        print('Validation Error:', flowerpost_to_create.errors)
        return Response(flowerpost_to_create.errors, 400)


class FlowerPostRetrieveUpdateDestroyView(APIView):
    permission_classes = [IsOwnerOrReadOnly]
    #Retrieve: Method GET
    @handle_exceptions
    def get(self, request, pk):
        flowerpost = FlowerPost.objects.get(pk=pk)
        serialized_flowerpost = PopulatedFlowerPostSerializer(flowerpost)
        #print('captured value:', id)
        return Response(serialized_flowerpost.data)
    

    #Update: Method PUT
    @handle_exceptions
    def put(self, request, pk):
        flowerpost_to_update = FlowerPost.objects.get(pk=pk)
        self.check_object_permissions(request, flowerpost_to_update)
        serialized_flowerpost = FlowerPostSerializer(flowerpost_to_update, data=request.data, partial=True)
        if serialized_flowerpost.is_valid():
            serialized_flowerpost.save()
            return Response(serialized_flowerpost.data)
        return Response(serialized_flowerpost.errors,400)


    #Destroy: Method DELETE
    @handle_exceptions
    def delete(self, request, pk):
        flowerpost_to_delete = FlowerPost.objects.get(pk=pk)
        self.check_object_permissions(request, flowerpost_to_delete)
        flowerpost_to_delete.delete()
        return Response(status=204)

    