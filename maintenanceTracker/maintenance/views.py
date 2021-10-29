from django.shortcuts import render

def home(request):
    return render(request, 'maintenance/home.html')


def logs(request):
    return render(request, 'maintenance/logs.html')