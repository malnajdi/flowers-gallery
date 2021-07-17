from rest_framework import serializers
from gallery.models import Flower


class FlowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flower
        fields = '__all__'