from rest_framework import serializers
from .models import Rating


class RatingSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.author

    class Meta:
        model = Rating
        fields = [
            'id', 'server', 'rating', 'author',
            'created_date', 'is_owner'
        ]
