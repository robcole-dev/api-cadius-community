from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    is_owner = serializers.SerializerMethodField()
    server_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.author

    class Meta:
        model = Profile
        fields = [
            'id', 'author', 'screen_name', 'full_name',
            'created_date', 'last_modified', 'profile_image', 'is_owner',
            'server_count'
        ]
