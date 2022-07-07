from ipaddress import ip_address
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from django.db.models import Count
from app.models import Comment, Like, UserCount
from app.serializer import CommentSerializer, LikeSerializer, UserCountSerializer


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


class CountView(APIView):
    permission_classes = []

    def post(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
    
        serializer = UserCountSerializer(data={
            **request.data,
            "ip_address": ip,
        })

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(status=status.HTTP_200_OK)

    def get(self, request):
        count = UserCount.objects.all().values('app_id').annotate(total=Count('device_id'))
        return Response(count)
