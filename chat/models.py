from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Group(models.Model): 
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User )
    
    def get_members(self) : 
        return list(self.members.values_list("username" , flat=True))

class Message(models.Model) : 
    sender= models.ForeignKey(User , on_delete=models.CASCADE)
    body = models.TextField()
    group = models.ForeignKey(Group , on_delete= models.CASCADE)
    time = models.DateTimeField(auto_now=True)