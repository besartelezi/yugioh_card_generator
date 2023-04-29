from rest_framework import serializers
from .models import MonsterCard

class MonsterCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonsterCard
        fields = ["name", "attribute", "stars", "type", "description", "attack", "defense"]