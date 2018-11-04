from django.shortcuts import render
from django.http import JsonResponse

def dashboard(request):
    return render(request , 'html/dashboard.html')
