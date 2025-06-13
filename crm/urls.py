from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet, ContactViewSet, RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'contacts', ContactViewSet)

urlpatterns = [
    path('', include(router.urls)),

    # Auth Routes
    path('register/', RegisterView.as_view(), name='register'),                  # Signup
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),     # Login
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),          # Token refresh
]
