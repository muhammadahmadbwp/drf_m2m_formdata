from django.urls import path, include
from core import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'actor', views.ActorsViewSet, basename='actors-api')

urlpatterns = [
    path('', include(router.urls)),
]