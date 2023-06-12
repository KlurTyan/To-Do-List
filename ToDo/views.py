from django.shortcuts import render, redirect

from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import mixins, status
from rest_framework_simplejwt.views import TokenObtainSlidingView, TokenRefreshSlidingView
from rest_framework.generics import ListAPIView

from django.utils import timezone
from rest_framework.response import Response

from .serializers import AffairsSerializer, TokenObtainPairSerializer, TokenRefreshSerializer, GetUserSerializer, AffairDeleteSerializer
from .permisssions import IsClientorSAdmin
from .models import Affairs, User

#PERMISSION
class SuperAdminView(ListAPIView):
    permission_classes=[IsAuthenticated,IsClientorSAdmin] 

    def get(self, request, *args, **kwargs):
        return Response(data={'success':'Ты супер мега администратор)'}, status=status.HTTP_200_OK)
    
class ClientView(ListAPIView):
    permission_classes=[IsAuthenticated,IsClientorSAdmin] 

    def get(self, request, *args, **kwargs):
        return Response(data={'success':'Вы являетесь пользователем!)'}, status=status.HTTP_200_OK)

#TOKENS
class TokenObtainPairView(TokenObtainSlidingView):
    permission_classes = [AllowAny]
    serializer_class = TokenObtainPairSerializer
    def get_permissions(self):
        return super().get_permissions()

class TokenRefreshView(TokenRefreshSlidingView):
    permission_classes = [AllowAny]
    serializer_class = TokenRefreshSerializer

#USER

class UserView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = GetUserSerializer
    queryset = User.objects.all()

    def get_current_user(self, request, *args, **kwargs):
        serializer = self.get_serializer(request.user)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

#AFFAIRS
class AffairViewSet(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    serializer_class = AffairsSerializer
    queryset = Affairs.objects.all()

    permission_classes = [AllowAny]

class AffairViewDelete(GenericViewSet, mixins.DestroyModelMixin):
    serializer_class = AffairDeleteSerializer
    queryset = Affairs.objects.all()

    permission_classes = [IsAuthenticated, IsClientorSAdmin]

def index(request):
    time = str(timezone.now().date())
    # processing a POST request
    if request.method == 'POST':
        add_task = request.POST.get('affair') # getting data from a POST request
        Affairs.objects.create(text = add_task,
                               date = time,
                               done = False) # saving data in the model
        return redirect('main')
    else:
        # processing a GET request
        objects = Affairs.objects.all()
        data = {
            'affair' : objects,
        }
        return render(request, 'index.html', data)
