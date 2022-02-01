from django.shortcuts import render
from urllib import request
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request, 'home.html')
