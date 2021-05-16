from django.contrib.auth.models import User
from accounts.models import CustomUser
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from blog.models import Blog, Category
from .serializers import BlogSerializer, CategorySerializer, UserSerializer

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# カテゴリーごとに記事を返す
class CategorizedBlogViewSet(generics.ListAPIView):
    serializer_class = BlogSerializer

    def get_queryset(self):
        queryset = Blog.objects.all()
        category_id = self.kwargs['category']
        category = Category.objects.get(id=category_id)
        queryset = queryset.filter(category=category)
        return queryset

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
