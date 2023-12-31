from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from .forms import SignUpForms

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForms(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            return redirect('home')
    else:
        form = SignUpForms()
    return render(request,'signup.html',{'form':form})
