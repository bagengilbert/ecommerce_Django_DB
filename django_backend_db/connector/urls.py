from django.urls import path, include
from rest_framework import routers
from .views import (ProductViewSet, UserViewSet, VendorViewSet, CategoryViewSet, OrderViewSet, OrderItemViewSet, PaymentViewSet,
                    ReviewViewSet, BlogViewSet, CartViewSet, CartItemViewSet, WishlistViewSet, ShippingViewSet, AnalyticsViewSet,
                    RefundViewSet, ConfigurationViewSet, FAQViewSet, SubscriptionViewSet, CouponViewSet, TaxViewSet,
                    NotificationViewSet, ContactViewSet)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'vendor', VendorViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'carts', CartViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'blogs', BlogViewSet)
router.register(r'coupons', CouponViewSet)
router.register(r'cart-item', CartItemViewSet)
router.register(r'wishlists', WishlistViewSet)
router.register(r'notifications', NotificationViewSet)
router.register(r'refunds', RefundViewSet)
router.register(r'configurations', ConfigurationViewSet)
router.register(r'contacts', ContactViewSet)
router.register(r'faqs', FAQViewSet)
router.register(r'order-item', OrderItemViewSet)
router.register(r'payments', PaymentViewSet)
router.register(r'shippings', ShippingViewSet)
router.register(r'taxes', TaxViewSet)
router.register(r'analytics', AnalyticsViewSet)
router.register(r'subscriptions', SubscriptionViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
