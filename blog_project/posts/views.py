from rest_framework import generics

from .models import Post
from .serializers import PostSerializer
from .permissions import IsAuthororReadOnly

from django.contrib.auth import get_user_model
""" from rest_framework import viewsets 
 """
from .models import Post
from .permissions import IsAuthororReadOnly
from .serializers import PostSerializer, UserSerializer # new

""" #views made using viewsets
class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthororReadOnly),
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer """



# Create your old views here.
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthororReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserList(generics.ListCreateAPIView): # new
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView): # new
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer







