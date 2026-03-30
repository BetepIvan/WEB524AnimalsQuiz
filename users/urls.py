from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from django.views.decorators.cache import never_cache

from users.apps import UsersConfig
from users.views import UserListAPIView, UserCreateAPIView, UserRetrieveAPIView, UserUpdateAPIView, UserDestroyAPIView, UserTokenObtainPairView


app_name = UsersConfig.name

urlpatterns = [
    # users urlpatterns
    path('', UserListAPIView.as_view(), name='users_list'),
    path('create/', UserCreateAPIView.as_view(), name='users_create'),
    path('<int:pk>/', UserRetrieveAPIView.as_view(), name='users_retrieve'),
    path('<int:pk>/update/', UserUpdateAPIView.as_view(), name='users_update'),
    path('<int:pk>/delete/', UserDestroyAPIView.as_view(), name='users_delete'),
]
