from django.contrib import admin
from .models import (
    Product, User, Order, OrderItem, Cart, CartItem, Wishlist,
    Review, ShippingAddress, AdminActivity, Media,
    NewsletterSubscription, Discount, LoyaltyPoint,
    Referral, DistributionPartnership, Influencer, SupportTicket
)

admin.site.register(Product)
admin.site.register(User)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Wishlist)
admin.site.register(Review)
admin.site.register(ShippingAddress)
admin.site.register(AdminActivity)
admin.site.register(Media)
admin.site.register(NewsletterSubscription)
admin.site.register(Discount)
admin.site.register(LoyaltyPoint)
admin.site.register(Referral)
admin.site.register(DistributionPartnership)
admin.site.register(Influencer)
admin.site.register(SupportTicket)
