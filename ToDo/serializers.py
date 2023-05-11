from rest_framework import serializers
from .models import Affairs

class AffairsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Affairs
        fields = '__all__'