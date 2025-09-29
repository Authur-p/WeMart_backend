from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from user_app.api.views import buyerRegistration, vendorRegistration, deliveryRegistration, logout


urlpatterns = [

    # path('login/', obtain_auth_token, name='login'),
    path('register-buyer/', buyerRegistration, name='register-buyer'),
    path('register-vendor/', vendorRegistration, name='register-vendor'),
    path('register-delivery/', deliveryRegistration, name='register-delivery'),
    path('logout/', logout, name='logout'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]