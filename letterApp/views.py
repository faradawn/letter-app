from django.http import HttpResponse

def about(request):
    return HttpResponse('This is about us')

def index(request):
    return HttpResponse('Welcome to Index')