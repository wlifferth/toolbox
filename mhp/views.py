from .forms import MHPSignUpForm
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login, authenticate

# Create your views here.
def index(request):
    return redirect('/tools/', context={})

def signup(request):
    if request.method == 'POST':
        return redirect('mhp:index')
        form = MHPSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mhp:index')
    else:
        form = MHPSignUpForm()
    return render(request, 'mhp/mhp_signup.html', {'form': form})
