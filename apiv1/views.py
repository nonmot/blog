from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from blog.models import Blog
from .serializers import BlogSerializer

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]