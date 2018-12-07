from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView
from .serializers import PostSerializer
from posts.models import Post


class PostViewSet(viewsets.ModelViewSet):
    
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)


class LikeToggleAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, pk):
        post_qs = Post.objects.filter(pk=pk)
        message = "Not allowed"
        if request.user.is_authenticated:
            is_liked = Post.objects.like_toggle(request.user, post_qs.first())
            return Response({'liked': is_liked})
        return Response({"message": message}, status=400)
        

class UnlikeToggleAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, pk):
        post_qs = Post.objects.filter(pk=pk)
        message = "Not allowed"
        if request.user.is_authenticated:
            is_unliked = Post.objects.unlike_toggle(request.user, 
                                                    post_qs.first())
            return Response({'liked': is_unliked})
        return Response({"message": message}, status=400)

posts_list = PostViewSet.as_view({
    'get': 'list',
    'post': 'create'})
