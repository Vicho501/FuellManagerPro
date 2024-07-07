from django.urls import path, include
from rest_framework import routers
from rest import views


router = routers.DefaultRouter()
router.register(r'produccions',views.ProduccionViewSet)
router.register(r'plantas',views.PlantaViewSet)
router.register(r'productos',views.ProductoViewSet)

urlpatterns = [path('', include(router.urls))]