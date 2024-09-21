from django.shortcuts import render
from rest_framework import viewsets
from .models import(User,Vendor,Product, Category,Order,OrderItem,Payment, 
                    Review,Coupon,Cart,CartItem,Wishlist,Shipping, 
                    Notification, Blog,Contact,FAQ,Analytics,
                    Tax,Subscription,Payment,Refund,Configuration,
                    Refund,Configuration)
from .serializers import(ProductSerializer, UserSerializer, VendorSerializer, CategorySerializer, OrderSerializer, OrderItemSerializer, PaymentSerializer,
                        ReviewSerializer, BlogSerializer, CartSerializer,CartItemSerializer, WishlistSerializer, ShippingSerializer, AnalyticsSerializer,
                        RefundSerializer, ConfigurationSerializer, FAQSerializer, SubscriptionSerializer, CouponSerializer, TaxSerializer,
                        NotificationSerializer, ContactSerializer)
User
User
User
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
 
class BlogViewSet(viewsets.ModelViewSet):
    queryset =Blog.objects.all()
    serializer_class =BlogSerializer

class CouponViewSet(viewsets.ModelViewSet):
    queryset =Coupon.objects.all()
    serializer_class =CouponSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset =Cart.objects.all()
    serializer_class =CartSerializer

class CartItemViewSet(viewsets.ModelViewSet):
    queryset =CartItem.objects.all()
    serializer_class =CartItemSerializer
    
class RefundViewSet(viewsets.ModelViewSet):
    queryset =Refund.objects.all()
    serializer_class =RefundSerializer

class ConfigurationViewSet(viewsets.ModelViewSet):
    queryset =Configuration.objects.all()
    serializer_class =ConfigurationSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    queryset =Notification.objects.all()
    serializer_class =NotificationSerializer

class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset =Subscription.objects.all()
    serializer_class =SubscriptionSerializer

class TaxViewSet(viewsets.ModelViewSet):
    queryset =Tax.objects.all()
    serializer_class =TaxSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset =Contact.objects.all()
    serializer_class =ContactSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset =Payment.objects.all()
    serializer_class =PaymentSerializer

class FAQViewSet(viewsets.ModelViewSet):
    queryset =FAQ.objects.all()
    serializer_class =FAQSerializer

class AnalyticsViewSet(viewsets.ModelViewSet):
    queryset =Analytics.objects.all()
    serializer_class =AnalyticsSerializer

class WishlistViewSet(viewsets.ModelViewSet):
    queryset =Wishlist.objects.all()
    serializer_class =WishlistSerializer

class ShippingViewSet(viewsets.ModelViewSet):
    queryset =Shipping.objects.all()
    serializer_class =ShippingSerializer