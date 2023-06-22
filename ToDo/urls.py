from django.urls import path, include

from rest_framework.routers import DefaultRouter

from ToDo.views import index, login_form, AffairViewSet, TokenObtainPairView, TokenRefreshView, SuperAdminView, ClientView, UserView, UserRegisterView, AffairViewGet, profile

router = DefaultRouter()
router.register('post',AffairViewSet, basename='post')

router_user = DefaultRouter()
router_user.register('register', UserRegisterView, basename='register')

urlpatterns = [
    path('', index, name='main'),
    path('login/', login_form, name='login_form'),
    path('profile/', profile, name='profile'),
    path('api/', include(router.urls)),
    path('api/posts/', AffairViewGet.as_view({'get':'list'})),
    # Tokens
    path('token/',TokenObtainPairView.as_view()),
    path('token/refresh/',TokenRefreshView.as_view()),
    
    # CLient
    path('user/Client/', ClientView.as_view()),
    path('user/SuperAdmin/', SuperAdminView.as_view()),
    path('user/me', UserView.as_view({'get':'get_current_user'})),
    path('user/', include(router_user.urls))
]
