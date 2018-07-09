from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
# Create your views here.
def sign_up(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            new_user = User.objects.create_user(username=username, password=password)
            user=authenticate(username=username,password=password)
            login(request,user)
            return HttpResponseRedirect('/')
    return render(request, 'registration.html',{'form':form})
