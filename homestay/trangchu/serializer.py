from rest_framework import serializers
from .models import *
# serializer use to return json

class RoomSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Phong
        fields = '__all__'

