from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    author_id = serializers.ReadOnlyField(source='author.profile.id')
    author_image = serializers.ReadOnlyField(
        source='author.profile.profile_image.url')
    is_owner = serializers.SerializerMethodField()
    created_date = serializers.SerializerMethodField()
    last_modified = serializers.SerializerMethodField()

    def get_created_date(self, obj):
        return naturaltime(obj.created_date)

    def get_last_modified(self, obj):
        return naturaltime(obj.last_modified)

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.author

    class Meta:
        model = Comment
        fields = [
            'id', 'screenshot', 'description', 'author', 'created_date',
            'last_modified', 'is_owner', 'author_id', 'author_image'
        ]


class CommentDetailSerializer(CommentSerializer):
    screenshot = serializers.ReadOnlyField(source='screenshot.id')
