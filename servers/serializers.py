from rest_framework import serializers
from .models import Server
from ratings.models import Rating


class ServerSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    author_id = serializers.ReadOnlyField(source='author.profile.id')
    author_image = serializers.ReadOnlyField(source='author.profile.image.url')
    is_owner = serializers.SerializerMethodField()
    avg_rating = serializers.ReadOnlyField()

    def validate_image(self, value):
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'Image size larger than 2MB, Please select another image.'
            )
        if value.image.width > 468:
            raise serializers.ValidationError(
                'Image is wider than 468px, please select another image.'
            )
        if value.image.height > 60:
            raise serializers.ValidationError(
                'Image is higher than 60px, please select another image'
            )
        return value

    def validate_game(self, value):
        if value == 'pick':
            raise serializers.ValidationError(
                'Please select a Game.'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.author

    class Meta:
        model = Server
        fields = [
            'id', 'game', 'server_name', 'server_address', 'author',
            'created_date', 'avg_rating', 'banner', 'is_owner',
            'author_id', 'author_image'
        ]
