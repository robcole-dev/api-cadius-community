from rest_framework import serializers
from .models import Tutorial


class TutorialSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    is_owner = serializers.SerializerMethodField()
    created_date = serializers.SerializerMethodField()
    last_modified = serializers.SerializerMethodField()

    def get_created_date(self, obj):
        return naturaltime(obj.created_date)
    
    def get_last_modified(self, obj):
        return naturaltime(obj.last_modified)

    def validate_video(self, value):
        if value.size > 1024 * 1024 * 100:
            raise serializers.ValidationError(
                'Video is larger than 100MB, Please select another video.'
            )
        return value
    
    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.author

    class Meta:
        model = Tutorial
        fields = [
            'id', 'title', 'description', 'video', 'image',
            'author', 'created_date', 'last_modified', 'is_owner'
        ]