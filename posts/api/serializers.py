from rest_framework import serializers
from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
 
    class Meta(object):
        model = Post
        fields = ('id', 'text', 'user', 'timestamp', 'updated', 'liked', 'unliked')
