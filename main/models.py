from django.db import models
from django.contrib.auth.models import User

class Tool(models.Model):
    def __str__(self):
        return self.name
    toolID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    description = models.TextField()
    category = models.CharField(max_length=100, choices=[('writing', 'writing'), ('physical', 'physical'), ('check', 'check')])
    icon = models.CharField(max_length=100, choices=[('glyphicon glyphicon-pencil', 'writing'), ('glyphicon glyphicon-flash', 'physical'), ('glyphicon glyphicon-check', 'check')])
    link = models.CharField(max_length=100)

class Client(models.Model):
    def __str__(self):
        return self.name
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    MHPID = models.ForeignKey('MHP', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    
class MHP(models.Model):
    def __str__(self):
        return self.name
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    
class Assignment(models.Model):
    def __str__(self):
        return "{}: {}".format(clientID, toolID)
    clientID = models.ForeignKey(Client, on_delete=models.CASCADE)
    toolID = models.ForeignKey(Tool, on_delete=models.CASCADE)
    notes = models.TextField()
