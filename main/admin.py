from django.contrib import admin
from .models import Tool, Client, MHP, Assignment

# Register your models here.
admin.site.register(Tool)
admin.site.register(Client)
admin.site.register(MHP)
admin.site.register(Assignment)
