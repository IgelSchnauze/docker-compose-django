from django.shortcuts import render
from simple_django.settings import DATABASES

def checkhost(request):
    hostname = f'{DATABASES["default"]["HOST"]}' + "web2"
    return render(request, 'checkhost.html', context = {'host': hostname},)