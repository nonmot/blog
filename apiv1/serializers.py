from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from blog.models import Blog, Category
from accounts.models import CustomUser

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'image', 'profile']

    def validate_password(self, value:str) -> str:
        return make_password(value)
