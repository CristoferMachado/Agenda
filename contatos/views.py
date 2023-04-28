from django.shortcuts import render , HttpResponse

def index(request):
    x=10+10
    return render(request,'pages/index.html',{'x':x})
