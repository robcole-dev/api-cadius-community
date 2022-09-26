from rest_framework import serializers
from .models import Emoji


class EmojiSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.author

    class Meta:
        model = Emoji
        fields = [
            'id', 'tutorial', 'emoji', 'author', 'created_date', 'is_owner'
        ]