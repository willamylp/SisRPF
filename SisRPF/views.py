from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from urllib import request

@login_required
def logoutApp(request):
    return render(request, 'loading/logoutApp.html')

@login_required
def loadApp(request):
    return render(request, 'loading/loadApp.html')
