from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from app.models import Comment
from app.serializer import CommentSerializer


class CommentView(APIView):
    permission_classes = []

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if not serializer.is_valid():
            Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()

        return Response(status=status.HTTP_200_OK)

    def get(self, request):
        data = request.GET

        comments = Comment.objects.all()
        if 'image_id' in data:
            comments = comments.filter(image_id=data['image_id'])

        serializer = CommentSerializer(comments, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
