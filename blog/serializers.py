from rest_framework import serializers
from .models import Blog, Comment

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model: Blog
        fields=['id', 'title', 'description', 'image_path','created_at', 'user', 'comments']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model:Comment
        fields=['id', 'text', 'date']

    