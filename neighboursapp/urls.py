from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import UserViewSet
from django.contrib.auth.views import LoginView, LogoutView 
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
router = routers.DefaultRouter(trailing_slash=False)
router.register('users', UserViewSet)
# router.register('hoods', HoodViewset)

# Users
user_signup = UserViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
urlpatterns = [
    path('auth/signup/', user_signup, name='user_signup'),
    path('api/adminprofile/', views.AdminProfileList.as_view(),name='adminprofiles'),
    path('api/hoodlist/', views.HoodList.as_view(),name='neighborhood'),
    path('api/residentlist/', views.ResidentList.as_view(),name='occupant'),
    # path('api/business/', views.BusinessList.as_view(),name='business'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('logout/',views.LogoutAPIView.as_view(),name='logout'),
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 