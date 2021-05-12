from django.test import TestCase

from accounts.models import CustomUser
from .models import Blog, Category

class BlogTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        user = cls.create_user()
        category = cls.create_category()
        cls.create_blog(user, category)

    # テストユーザーの作成
    @classmethod
    def create_user(cls):
        CustomUser(username="test", password="test").save()
        user = CustomUser.objects.filter(username="test").first()
        return user

    # テスト記事の作成
    @classmethod
    def create_blog(cls, user, category):
        Blog(title="test", content="test", user_id=user.id).save()
        blog = Blog.objects.filter(title="test").first()
        blog.category.set(category)
        return blog

    # テストカテゴリーの作成
    @classmethod
    def create_category(cls):
        Category(name="test").save()
        category = Category.objects.filter(name="test")
        return category

    # ユーザーが存在するか
    def test_user_should_be_present(self):
        user = CustomUser.objects.first()
        self.assertIsNotNone(user)

    # 記事が存在するか
    def test_blog_should_be_present(self):
        blog = Blog.objects.first()
        self.assertIsNotNone(blog)

