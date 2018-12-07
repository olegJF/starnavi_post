from django.urls import path
from posts.api.views import LikeToggleAPIView, UnlikeToggleAPIView
from posts.api.views import posts_list


urlpatterns = [
    path('like/<int:pk>/', LikeToggleAPIView.as_view(), name='like_api'),
    path('unlike/<int:pk>/', UnlikeToggleAPIView.as_view(), name='unlike_api'),
    path('', posts_list, name='posts_list'),
]
