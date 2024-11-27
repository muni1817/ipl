from django.shortcuts import render
from django.http import HttpResponse
def rcb(request):
    return HttpResponse('<h1>virat kohli is captain of rcb</h1>')
