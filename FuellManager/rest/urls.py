from django.urls import path, include
from rest_framework import serializers, routers
from . import views
from .views import ProduccionViewSet

router = routers.DefaultRouter()
router.register('produccions',views.ProduccionViewSet)

urlpatterns = router.urls