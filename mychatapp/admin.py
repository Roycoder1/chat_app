from django.contrib import admin
from .models import  Friend, ChatMessage,UserProfile

# Register your models here.
admin.site.register([ Friend, ChatMessage,UserProfile])