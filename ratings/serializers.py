from rest_framework import serializers
from .models import Rating

class RatingSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    is_owner = serializers.SerializerMethodField()

    class Meta:
        model = Rating
        fields = [
            'id', 'server', 'one', 'two', 'three', 'four', 'five', 'is_owner'
        ]