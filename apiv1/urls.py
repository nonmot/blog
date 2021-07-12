from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('blog', views.BlogViewSet)
router.register('category', views.CategoryViewSet)
router.register('user', views.UserViewSet)


app_name = 'apiv1'

urlpatterns = [
    path('', include(router.urls)),
    path('blog/category/<str:category>/', views.CategorizedBlogViewSet.as_view())
]