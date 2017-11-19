from django.shortcuts import render

class Tool:
    def __init__(self, name="Name", slug="name", description="description", category="writing"):
        self.name = name
        self.slug = slug
        self.link = slug + ':index'
        self.description = description
        if category == "writing":
            self.icon = "glyphicon glyphicon-pencil"
        elif category == "physical":
            self.icon = "glyphicon glyphicon-flash"
        elif category == "check":
            self.icon = "glyphicon glyphicon-check"

# Create your views here.
def index(request):
    tool = Tool(name="Guided Breathing", slug="guided_breathing", description="An exercise that will help you slow down your breathing, lower your heart rate, and relax.")
    tools = [tool, tool, tool]
    context = {}
    context['tools'] = tools
    return render(request, 'tools/tools.html', context=context)
