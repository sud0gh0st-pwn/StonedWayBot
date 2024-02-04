from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuItemViewSet, CartViewSet, CartItemViewSet, OrderViewSet

router = DefaultRouter()
router.register(r'menuitems', MenuItemViewSet)
router.register(r'carts', CartViewSet)
router.register(r'cartitems', CartItemViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
