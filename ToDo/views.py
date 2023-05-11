from django.shortcuts import render, redirect
from .models import Affairs

from rest_framework.viewsets import GenericViewSet
from .serializers import AffairsSerializer
from rest_framework import mixins

from datetime import datetime

class AffairViewSet(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    serializer_class = AffairsSerializer
    queryset = Affairs.objects.all()

def index(request):
    time = str(datetime.now().date())
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
