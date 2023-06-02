from django.urls import path, include
from .views import UserViewSet
from rest_framework import routers
from rest_framework.documentation import include_docs_urls


router = routers.DefaultRouter()
router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('api/', include(router.urls)),
    path('docs/', include_docs_urls(title='Django users CRUD API')),
    
]
