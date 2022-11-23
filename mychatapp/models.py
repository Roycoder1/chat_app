import profile
from xmlrpc.client import Boolean
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=60, null=True, blank=True)
    last_name = models.CharField(max_length=60, null=True, blank=True)
    email = models.EmailField( null=True, blank=True)
    born_date= models.DateField( null=True, blank=True)
    age = models.IntegerField( null=True, blank=True)
    phone_number = models.IntegerField( null=True, blank=True)
    friends = models.ManyToManyField('Friend')
    
    
    def __str__(self) -> str:
        return f'{self.first_name} { self.last_name}'
    
class Friend(models.Model):
    profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return self.profile.name

class ChatMessage(models.Model):
    subject=models.CharField(max_length=300)
    body = models.TextField()
    msg_sender = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="msg_sender")
    msg_receiver = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="msg_receiver")
    seen = models.BooleanField(default=False)
    creation_date=models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
        return self.body
    
