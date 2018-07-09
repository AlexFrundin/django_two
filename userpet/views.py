from django.shortcuts import render
from django.http import HttpResponse

# def test(request):
#     return HttpResponse("Hello!")
def home(request):
    return render(request,"home.html",{'data':"Hello"})
