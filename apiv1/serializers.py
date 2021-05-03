from rest_framework import serializers
import markdown

from blog.models import Blog

class BlogSerializer(serializers.ModelSerializer):
    content = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = ['id', 'title', 'content']

    def get_content(self, instance):
        return markdown.markdown(instance.content, extensions=['markdown.extensions.toc'])