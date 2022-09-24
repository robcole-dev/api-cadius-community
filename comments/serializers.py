from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.author
    
    class Meta:
        model = Comment
        fields = [
            'id', 'tutorial', 'description', 'author', 'created_date',
            'last_modified', 'is_owner' 
        ]