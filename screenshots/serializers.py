from rest_framework import serializers
from .models import Screenshot


class ScreenshotSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    author_id = serializers.ReadOnlyField(source='author.profile.id')
    author_image = serializers.ReadOnlyField(source='author.profile.image.url')

    is_owner = serializers.SerializerMethodField()

    def validate_image(self, value):
        if value.size > 1024 * 1024 * 10:
            raise serializers.ValidationError(
                'Image size larger than 10MB, Please select another image.'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.author

    class Meta:
        model = Screenshot
        fields = [
            'id', 'title', 'description', 'image',
            'author', 'created_date', 'last_modified', 'is_owner',
            'author_id', 'author_image'
        ]
