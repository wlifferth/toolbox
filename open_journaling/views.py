from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'open_journaling/open_journaling.html', context={});

def submit(request):
    return redirect('tools:index')
