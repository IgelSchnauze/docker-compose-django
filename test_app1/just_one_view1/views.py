from django.shortcuts import render
from simple_django.settings import DATABASES

def checkhost(request):
    hostname = f'{DATABASES["default"]["HOST"]}' + "web1"
    return render(request, 'checkhost.html', context = {'host': hostname},)