from django.urls import path, include
from rest_framework import routers 
from . views import (ProductViewSet, UserViewSet, VendorViewSet, CategoryViewSet, OrderViewSet, OrderItemViewSet, PaymentViewSet,
                        ReviewViewSet, BlogViewSet, CartViewSet,CartItemViewSet, WishlistViewSet, ShippingViewSet, AnalyticsViewSet,
                        RefundViewSet, ConfigurationViewSet, FAQViewSet, SubscriptionViewSet, CouponViewSet, TaxViewSet,
                        NotificationViewSet, ContactViewSet)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'products', ProductViewSet)
router.register(r'vendor', VendorViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'order',OrderViewSet)
router.register(r'order-item', OrderItemViewSet)
router.register(r'payment', PaymentViewSet)
router.register(r'review', ReviewViewSet)
router.register(r'blog',BlogViewSet)
router.register(r'cart', CartViewSet)
router.register(r'refund', RefundViewSet)
router.register(r'cart-item', CartItemViewSet)
router.register(r'wishlist', WishlistViewSet)
router.register(r'shipping',ShippingViewSet)
router.register(r'analytics', AnalyticsViewSet)
router.register(r'configuration', ConfigurationViewSet)
router.register(r'faq', FAQViewSet)
router.register(r'subscription', SubscriptionViewSet)
router.register(r'coupon',CouponViewSet)
router.register(r'taxview', TaxViewSet)
router.register(r'notification', NotificationViewSet)
router.register(r'contact', ContactViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
