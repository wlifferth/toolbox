from django.shortcuts import render

from main.models import Tool

# Create your views here.
def index(request):
    tools = [Tool.objects.get()]
    context = {}
    context['tools'] = tools
    return render(request, 'tools/tools.html', context=context)
