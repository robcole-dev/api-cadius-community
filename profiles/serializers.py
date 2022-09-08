from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='username.username')

    class Meta:
        model = Profile
        fields = [
            'id', 'username', 'screen_name', 'created_date', 'last_modified',
            'profile_image'
        ]
