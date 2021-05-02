from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('blog', views.BlogViewSet)

app_name = 'apiv1'

urlpatterns = [
    path('', include(router.urls))
]