from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FlowerPost
from .serializers.common import FlowerPostSerializer

# Create your views here.
class FlowerPostListCreateView(APIView):
    #INDEX Route
    def get(self, request):
        flowerposts = FlowerPost.objects.all()
        serialized_flowerposts = FlowerPostSerializer(flowerposts, many=True)
        print(serialized_flowerposts.data)
        return Response(serialized_flowerposts.data)
    
    #CREATE Route
    def post(self, request):
        try:
            flowerpost_to_create = FlowerPostSerializer(data=request.data)
            if flowerpost_to_create.is_valid():
                #data is valid
                flowerpost_to_create.save()
                return Response(flowerpost_to_create.data, 201)
            
            #error occurred during validation
            print('validation error:', flowerpost_to_create.errors)
            return Response(flowerpost_to_create.errors, 400)
        except Exception as e:
            print('error:', e)
            return Response('an error occurred', 500)


class FlowerPostRetrieveUpdateDestroyView(APIView):
    #Retrieve: Method GET
    def get(self, request, id):
        try:
            flowerpost = FlowerPost.objects.get(pk=id)
            serialized_flowerpost = FlowerPostSerializer(flowerpost)
            #print('captured value:', id)
            return Response(serialized_flowerpost.data)
        except FlowerPost.DoesNotExist as e:
            print(e)
            return Response({'message': 'Flower post not found'}, 404)
        except Exception as e:
            print(e.__class__.__name__)
            return Response({'message': 'An error occurred'}, 500)

    #Update: Method PUT
    def put(self, request, id):
        try:
            flowerpost_to_update = FlowerPost.objects.get(pk=id)
            serialized_flowerpost = FlowerPostSerializer(flowerpost_to_update, data=request.data, partial=True)
            if serialized_flowerpost.is_valid():
                serialized_flowerpost.save()
                return Response(serialized_flowerpost.data)
            return Response(serialized_flowerpost.errors,400)
        except FlowerPost.DoesNotExist as e:
            print(e)
            return Response('flowerpost not found', 404)
        except Exception as e:
            print(e)
            return Response('an unknown error occurred', 500)

    #Destroy: Method DELETE
    