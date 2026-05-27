from django.contrib import admin
from django.urls import path,include
from inventory.views import ProductViewSet,SalesViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('products',ProductViewSet)
router.register('sales',SalesViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    
]