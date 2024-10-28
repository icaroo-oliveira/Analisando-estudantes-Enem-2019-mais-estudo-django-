from django.http import HttpResponse
from django.shortcuts import render




def dashboard(request):
    return render(request, 'dashboard.html')  


def home(request):
    return render(request, 'home.html')  

def sobre(request):
    return render(request, 'sobre.html')  