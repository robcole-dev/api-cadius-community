from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='username.username')
    is_owner = serializers.SerializerMethodField()
    server_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.username

    class Meta:
        model = Profile
        fields = [
            'id', 'username', 'screen_name', 'full_name', 'last_name',
            'created_date', 'last_modified', 'profile_image', 'is_owner',
            'server_count'
        ]
