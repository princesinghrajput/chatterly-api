from rest_framework import serializers
from .models import Blog, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields=['id', 'text', 'date']

class BlogSerializer(serializers.ModelSerializer):
    comments= CommentSerializer(many=True, read_only=True)
    class Meta:
        model=Blog
        fields=['id','user', 'title', 'description', 'image_path', 'created_at', 'comments']
   

