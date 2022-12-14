from django.shortcuts import render
from .models import Post
from .serializers import PostSerializer
from rest_framework import generics
from .permissions import IsAuthorOrReadOnly


class PostList(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# Create your views here.
