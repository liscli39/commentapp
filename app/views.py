from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from app.models import Comment, Like
from app.serializer import CommentSerializer, LikeSerializer


class CommentView(APIView):
    permission_classes = []

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()

        return Response(status=status.HTTP_200_OK)

    def get(self, request):
        data = request.GET

        comments = Comment.objects.all()
        if 'image_id' in data:
            comments = comments.filter(image_id=data['image_id'])

        serializer = CommentSerializer(comments, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class LikeView(APIView):
    permission_classes = []

    def post(self, request):
        serializer = LikeSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()

        return Response(status=status.HTTP_200_OK)

    def get(self, request):
        data = request.GET

        likes = Like.objects.all()
        if 'image_id' in data:
            likes = likes.filter(image_id=data['image_id'])

        is_like = False
        if 'device_id' in data:
            is_like = likes.filter(device_id=data['device_id']).exists()

        return Response({ "count": likes.count(), "is_like": is_like }, status=status.HTTP_200_OK)
