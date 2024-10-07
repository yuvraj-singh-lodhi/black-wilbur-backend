from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (CategoryViewSet, ProductViewSet, ProductImageViewSet, ProductSizeViewSet, UserViewSet, 
                    OrderViewSet, OrderItemViewSet, CartViewSet, CartItemViewSet, 
                    WishlistViewSet, ReviewViewSet, ShippingAddressViewSet, MediaViewSet, 
                    NewsletterSubscriptionViewSet, DiscountViewSet, LoyaltyPointViewSet, 
                    ReferralViewSet, DistributionPartnershipViewSet, InfluencerViewSet, 
                    SupportTicketViewSet, RegisterView, LoginView,UserDetailsViewSet,get_current_user)
from rest_framework_simplejwt.views import TokenRefreshView

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'product-images', ProductImageViewSet)
router.register(r'product-sizes', ProductSizeViewSet)
router.register(r'users', UserViewSet)  # Ensure this is not duplicated elsewhere
router.register(r'orders', OrderViewSet)
router.register(r'order-items', OrderItemViewSet)
router.register(r'carts', CartViewSet)
router.register(r'cart-items', CartItemViewSet)
router.register(r'wishlists', WishlistViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'shipping-addresses', ShippingAddressViewSet)
router.register(r'media', MediaViewSet)
router.register(r'newsletter-subscriptions', NewsletterSubscriptionViewSet)
router.register(r'discounts', DiscountViewSet)
router.register(r'loyalty-points', LoyaltyPointViewSet)
router.register(r'referrals', ReferralViewSet)
router.register(r'distribution-partnerships', DistributionPartnershipViewSet)
router.register(r'influencers', InfluencerViewSet)
router.register(r'support-tickets', SupportTicketViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user-details/', UserDetailsViewSet.as_view({'get': 'retrieve'}), name='user-details'),
    path('current-user/', get_current_user, name='current-user'),

]
