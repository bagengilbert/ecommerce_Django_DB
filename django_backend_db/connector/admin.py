from django.contrib import admin

# Register your models here.
from .models import ( User, Vendor, Product, Category,Order,  OrderItem, Payment, 
                    Review, Coupon, Cart, CartItem, Wishlist, Shipping, 
                    Notification, Blog, Contact,FAQ, Analytics,
                    Tax,Subscription,  Refund, Configuration)

admin.site.register(User)
admin.site.register(Vendor)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Payment)
admin.site.register(Review)
admin.site.register(Coupon)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Wishlist)
admin.site.register(Shipping)
admin.site.register(Notification)
admin.site.register(Blog)
admin.site.register(Contact)
admin.site.register(FAQ)
admin.site.register(Analytics)
admin.site.register(Tax)
admin.site.register(Subscription)
admin.site.register(Refund)
admin.site.register(Configuration)
