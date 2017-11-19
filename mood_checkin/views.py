from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'mood_checkin/mood_checkin.html', context={})
