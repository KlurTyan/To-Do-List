from django.urls import path, include

from rest_framework.routers import DefaultRouter

from ToDo.views import index, AffairViewSet

router = DefaultRouter()
router.register('post',AffairViewSet, basename='post')

urlpatterns = [
    path('', index, name='main'),
    path('api/', include(router.urls)),

]
