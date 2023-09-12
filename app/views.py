from django.shortcuts import render
from app.models import *
from app.forms import *
from django.http import *
# Create your views here.

def coaching(request):
    ICD= Jspider()
    d= {'ICD':ICD}

    if request.method=='POST':
        ICDE=Jspider(request.POST)

        if ICDE.is_valid():
            return HttpResponse(str(ICDE.cleaned_data))
        return HttpResponse('Invalid Data')
    return render(request,'coaching_data.html', context=d)