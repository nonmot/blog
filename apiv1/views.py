from accounts.models import CustomUser
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from blog.models import Blog, Category
from .serializers import BlogSerializer, CategorySerializer, UserSerializer
from apiv1 import serializers
from .permissions import PublicOrSuperUser
from .filters import IsPublicOrSuperuser

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, PublicOrSuperUser]
    filter_backends = [IsPublicOrSuperuser]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# カテゴリーごとに記事を返す
class CategorizedBlogViewSet(generics.ListAPIView):
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, PublicOrSuperUser]
    filter_backends = [IsPublicOrSuperuser]

    def get_queryset(self):
        queryset = Blog.objects.all()
        category = self.kwargs['category']
        category = Category.objects.get(name=category)
        queryset = queryset.filter(category=category)
        return queryset

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def owner(self, request, **kwargs):
        user = CustomUser.objects.first()
        serializer = UserSerializer(user)
        return Response(serializer.data)
