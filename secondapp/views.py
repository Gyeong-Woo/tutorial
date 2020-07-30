from django.shortcuts import render
from django.http import HttpResponse



def h_name(request):
    return HttpResponse('<h1>Hello</h1>')

def show_h(request):
    hospital = Hospital.objects.all()
    return HttpResponse(hospital)