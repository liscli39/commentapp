from rest_framework import serializers
from app.models import Comment, Like, UserCount


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'


class UserCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCount
        fields = '__all__'
