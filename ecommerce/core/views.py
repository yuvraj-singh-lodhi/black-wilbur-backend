from django import views
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes  
from .models import (Category, Product, ProductImage, ProductSize, User, Order, 
                     OrderItem, Cart, CartItem, Wishlist, Review, ShippingAddress, 
                     Media, NewsletterSubscription, Discount, LoyaltyPoint, 
                     Referral, DistributionPartnership, Influencer, SupportTicket)
from .serializers import (CategorySerializer, ProductSerializer, ProductImageSerializer, 
                          ProductSizeSerializer, UserSerializer, OrderSerializer, 
                          OrderItemSerializer, CartSerializer, CartItemSerializer, 
                          WishlistSerializer, ReviewSerializer, ShippingAddressSerializer, 
                          MediaSerializer, NewsletterSubscriptionSerializer, 
                          DiscountSerializer, LoyaltyPointSerializer, ReferralSerializer, 
                          DistributionPartnershipSerializer, InfluencerSerializer, 
                          SupportTicketSerializer)
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterSerializer, LoginSerializer


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            refresh = RefreshToken.for_user(user)

            user_data = {
                'id': user.id,
                'username': user.username,
                'email': user.email,
            }

            return Response({
                'message': 'Login successful',
                'token': str(refresh.access_token),
                'user': user_data,
            }, status=status.HTTP_200_OK)

        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class UserDetailsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

    def retrieve(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user = self.get_object()
            user_data = UserSerializer(user).data
            
            cart_data = CartSerializer(user.cart).data if hasattr(user, 'cart') else {}
            wishlist_data = WishlistSerializer(user.wishlist).data if hasattr(user, 'wishlist') else {}
            orders_data = OrderSerializer(Order.objects.filter(user=user), many=True).data
            
            return Response({
                "user": user_data,
                "cart": cart_data,
                "wishlist": wishlist_data,
                "orders": orders_data,
            })
        else:
            return Response(
                {"error": "Authentication credentials were not provided."},
                status=status.HTTP_401_UNAUTHORIZED
            )

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_current_user(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer


class ProductSizeViewSet(viewsets.ModelViewSet):
    queryset = ProductSize.objects.all()
    serializer_class = ProductSizeSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        if user_id:
            return Order.objects.filter(user_id=user_id)
        return super().get_queryset()


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

    def get_queryset(self):
        order_id = self.request.query_params.get('order_id')
        if order_id:
            return OrderItem.objects.filter(order_id=order_id)
        return super().get_queryset()


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        if user_id:
            return Cart.objects.filter(user_id=user_id)
        return super().get_queryset()


class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def get_queryset(self):
        cart_id = self.request.query_params.get('cart_id')
        if cart_id:
            return CartItem.objects.filter(cart_id=cart_id)
        return super().get_queryset()


class WishlistViewSet(viewsets.ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        if user_id:
            return Wishlist.objects.filter(user_id=user_id)
        return super().get_queryset()


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        product_id = self.request.query_params.get('product_id')
        if product_id:
            return Review.objects.filter(product_id=product_id)
        return super().get_queryset()


class ShippingAddressViewSet(viewsets.ModelViewSet):
    queryset = ShippingAddress.objects.all()
    serializer_class = ShippingAddressSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        if user_id:
            return ShippingAddress.objects.filter(user_id=user_id)
        return super().get_queryset()


class MediaViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer


class NewsletterSubscriptionViewSet(viewsets.ModelViewSet):
    queryset = NewsletterSubscription.objects.all()
    serializer_class = NewsletterSubscriptionSerializer


class DiscountViewSet(viewsets.ModelViewSet):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer


class LoyaltyPointViewSet(viewsets.ModelViewSet):
    queryset = LoyaltyPoint.objects.all()
    serializer_class = LoyaltyPointSerializer


class ReferralViewSet(viewsets.ModelViewSet):
    queryset = Referral.objects.all()
    serializer_class = ReferralSerializer


class DistributionPartnershipViewSet(viewsets.ModelViewSet):
    queryset = DistributionPartnership.objects.all()
    serializer_class = DistributionPartnershipSerializer


class InfluencerViewSet(viewsets.ModelViewSet):
    queryset = Influencer.objects.all()
    serializer_class = InfluencerSerializer


class SupportTicketViewSet(viewsets.ModelViewSet):
    queryset = SupportTicket.objects.all()
    serializer_class = SupportTicketSerializer
