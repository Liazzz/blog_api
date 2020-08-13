from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializer


# @api_view()
# def posts_list(request):
#     queryset = Post.objects.all()
#     serializer = PostSerializer(queryset, many=True, context={'request': request})
#     return Response(data=serializer.data, status=status.HTTP_200_OK)


class PostListView(generics.ListAPIView):
    # def get(self, request, format=None):
    #     queryset = Post.objects.all()
    #     serializer = PostSerializer(queryset, many=True, context={'request': request})
    #     return Response(data=serializer.data, status=status.HTTP_200_OK)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailsView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CreatePostView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = PostSerializer(data=data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        post = serializer.save()
        # post.author = request.user
        # post.save()
        serializer = PostSerializer(instance=post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UpdatePostView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class DeletePostView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer