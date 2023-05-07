from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'image', views.ImageViewSet, basename = 'image')
router.register(r'history', views.UserHistoryViewSet, basename = 'history')


urlpatterns = [
    path('', include(router.urls)),    
]
