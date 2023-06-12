from django.urls import path, include

from rest_framework.routers import DefaultRouter

from ToDo.views import index, AffairViewSet, TokenObtainPairView, TokenRefreshView, SuperAdminView, ClientView, UserView, AffairViewDelete

router = DefaultRouter()
router.register('post',AffairViewSet, basename='post')
router.register('post-delete', AffairViewDelete, basename='delete-post')

urlpatterns = [
    path('', index, name='main'),
    path('api/', include(router.urls)), 
    # Tokens
    path('token/',TokenObtainPairView.as_view()),
    path('token/refresh/',TokenRefreshView.as_view()),
    
    # CLient
    path('user/client/', ClientView.as_view()),
    path('user/SuperAdmin/', SuperAdminView.as_view()),
    path('user/me', UserView.as_view({'get':'get_current_user'}))
]
