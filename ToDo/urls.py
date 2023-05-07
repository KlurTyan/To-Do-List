from django.urls import path

from ToDo.views import index

urlpatterns = [
    path('', index)
]
