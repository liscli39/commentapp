from django.urls import path, include

from . import views

urlpatterns = [
    path('comments', views.CommentView.as_view()),
    path('likes', views.LikeView.as_view()),
    path('count', views.CountView.as_view()),
]