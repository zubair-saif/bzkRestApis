from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('hello word')

def about(request):
    return HttpResponse('about page')    