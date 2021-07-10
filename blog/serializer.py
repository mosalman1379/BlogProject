from rest_framework import serializers
from blog.models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    """
    Serializer class for post
    """

    class Meta:
        model = Post
        fields = ('title', 'author', 'body', 'status')


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer class for comment
    """

    class Meta:
        model = Comment
        fields = ('name', 'email', 'body','post')
