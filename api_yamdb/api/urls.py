from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import signup, get_token, UserViewSet, MePage

router = DefaultRouter()

router.register(r'users', UserViewSet)

urlpatterns = [
    path('v1/users/me/', MePage.as_view()),
    path('v1/', include(router.urls)),
    path('v1/auth/signup/', signup),
    path('v1/auth/token/', get_token),
]