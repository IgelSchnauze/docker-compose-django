from django.shortcuts import render
from simple_django.settings import DATABASES

def checkhost(request):
    hostname = f'host: {DATABASES["default"]["HOST"]}'
    return render(request, 'checkhost.html', context = {'host': hostname},)