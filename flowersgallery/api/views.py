from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import FlowerSerializer

from gallery.models import Flower


class FlowerListAPIView(APIView):
    def get(self, request, format=None):
        flowers = Flower.objects.all()
        serialized_flowers = FlowerSerializer(flowers, many=True)
        return Response(serialized_flowers.data)


class FlowerDetailAPIView(APIView):
    def get(self, request, id, format=None):
        flower = Flower.objects.get(id=id)
        serialized_flower = FlowerSerializer(flower)
        return Response(serialized_flower.data)        