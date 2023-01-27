from django.shortcuts import render, HttpResponse

# Create your views here.
def index (request):
    return HttpResponse('<h1 style="background-color:yellow;"><center>configHack</center><h1>')
