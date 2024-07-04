from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .api import signup, me, users_list


urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('signup/', signup, name="signup"),
    path('me/', me, name="me"),
    path('userlist/', users_list, name="user_list"),

]