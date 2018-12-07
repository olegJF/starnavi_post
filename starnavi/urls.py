from django.contrib import admin
from django.urls import path, include
from accounts.views import UserSignUpView, login_view, logout_view
from posts.views import *
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', UserSignUpView.as_view(), name='signup'),
    path('create/', PostCreateView.as_view(), name='create'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('like/<int:pk>/', set_like, name='like'),
    path('unlike/<int:pk>/', set_unlike, name='unlike'),
    path('api/posts/', include('posts.api.urls')),
    path('api/users/', include('accounts.api.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('', post_view, name='home'),
]
