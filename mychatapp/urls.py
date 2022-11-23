from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView , LogoutView
from .views import get_unreadMessage,exercise_delete,allMessages,results,get_queryset,registerUsers,index,register,detail,sentMessages,receivedMessages
urlpatterns = [
    path("", LoginView.as_view(template_name = 'login.html'), name='login'),
    path('register', register , name='register'),
    path('friend/<int:id>', detail, name="detail"),
    path('sent_msg/<str:pk>', sentMessages, name = "sent_msg"),
    path('rec_msg/<str:pk>', receivedMessages, name = "rec_msg"),
    path('home', index, name= "home"),
    path('registration',registerUsers, name='registration'),
    path('search',get_queryset,name='search'),
    path('friends',results,name='friends'),
    path('message',allMessages,name='message'),
    path('delete_message/<int:id>',exercise_delete,name='delete'),
    path('unread',get_unreadMessage,name='unread')
    
    
]
