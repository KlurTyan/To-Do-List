from django.shortcuts import render, redirect
from .models import Affairs
from .forms import AffairsForm

from datetime import datetime
import re

def index(request):
    time = str(datetime.now().date())
    if request.method == 'POST':
        my_data =request.POST.get('affair', '')
        Affairs.objects.create(text = my_data,
                               date = time,
                               done = False)
        return redirect('main')
    else:
        my_data_list = Affairs.objects.all()
        return render(request, 'index.html', {'affair' : my_data_list})
    # affair = Affairs.objects.all() 
    # if request.method == 'POST':
    #     form = AffairsForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('main')
    #     form = AffairsForm
    #     data = {
    #         'form'
    #     }
    # else:
    #     form = AffairsForm
    # data = {'form' : 'form'}
    # return render(request, 'index.html', data)

    # # else:
    # #     return render(request, 'index.html', {'affair':affair})

    
    
    

    

