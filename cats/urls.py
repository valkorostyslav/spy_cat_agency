from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CatViewSet

# Створюємо роутер
router = DefaultRouter()
router.register(r'cats', CatViewSet, basename='cat')

urlpatterns = [
    path('', include(router.urls)),
]