from rest_framework import serializers

from .models import Spent

class SpentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spent
        fields = '__all__'