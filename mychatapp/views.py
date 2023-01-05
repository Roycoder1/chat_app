
from django.shortcuts import render, redirect
from .models import ChatMessage, Friend,UserProfile
from .forms import ChatMessageForm,UserProfilForm
from django.http import JsonResponse
import json
from django.contrib.auth.forms import UserCreationForm  

from django.contrib.auth.views import LoginView 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate,login,logout

from django.shortcuts import render, redirect
from .models import ChatMessage, Friend,UserProfile



from django.db.models import Q

# Create your views here.
def register(request):
    context = {'form': UserCreationForm}
    if request.method == 'POST':
        
        form_filled = UserCreationForm(request.POST)

        if form_filled.is_valid():

            form_filled.save()
            
            u_username = form_filled.cleaned_data['username']
            u_password = form_filled.cleaned_data['password1']
           
            user = authenticate(username = u_username, password = u_password)

            if user :
                login(request, user)
                return redirect('registration')
            else:
                print("User not authenticated")
        
        else:

            return render(request, 'register.html', {'form': form_filled})

    return render(request, 'register.html', context)


def registerUsers(request):
    player, created = UserProfile.objects.get_or_create(user=request.user)
    profile = request.user.userprofile
    form = UserProfilForm(request.POST or None, instance=profile)
    

    context = {'form': form }

    if form.is_valid():
        userprofile=form.save()
        
       

        
        return redirect('login')
    else:
        print(form.errors)
        
    
    
    return render(request,'registration.html',context)


def detail(request,id):
    user = request.user.userprofile
    
    if not Friend.objects.filter(profile_id=id).exists():
            Friend.objects.create(profile_id = id)   
    friend = Friend.objects.get(profile_id=id)
    
    profile = UserProfile.objects.get(id=friend.profile.id)
    chats = ChatMessage.objects.all()
    rec_chats = ChatMessage.objects.filter(msg_sender=profile, msg_receiver=user, seen=False)
    rec_chats.update(seen=True)
    form = ChatMessageForm()
    if request.method == "POST":
        form = ChatMessageForm(request.POST)
        if form.is_valid():
            chat_message = form.save(commit=False)
            chat_message.msg_sender = user
            chat_message.msg_receiver = profile
            chat_message.save()
            return redirect("detail", pk=friend.profile.id)
    context = {"friend": friend, "form": form, "user":user, 
               "profile":profile, "chats": chats, "num": rec_chats.count()}
    return render(request, "detail.html", context)

def sentMessages(request, pk):
    user = request.user.userprofile
    friend = Friend.objects.get(profile_id=pk)
    profile = UserProfile.objects.get(id=friend.profile.id)
    data = json.loads(request.body)
    
    
    
    new_chat = data["msg"]
    new_chat_message = ChatMessage.objects.create(body=new_chat, msg_sender=user, msg_receiver=profile, seen=False )
    print(new_chat)
    return JsonResponse(new_chat_message.body, safe=False)

def receivedMessages(request, pk):
    user = request.user.userprofile
    friend = Friend.objects.get(profile_id=pk)
    profile = UserProfile.objects.get(id=friend.profile.id)
    arr = []
    chats = ChatMessage.objects.filter(msg_sender=profile, msg_receiver=user)
    for chat in chats:
        arr.append(chat.body)
    return JsonResponse(arr, safe=False)




def index(request):
    user = request.user.userprofile
    
    friends = Friend.objects.all()
    
    context = {"user": user,'friends':friends}
    return render(request, "home.html", context)


def get_queryset(request):  # new
    search_post = request.POST.get('searchfirstname')
    
   
    return render(request, 'search.html')

def results(request):
# Query all posts
    search_post = request.POST.get('searchfirstname')
    
    

    if search_post:
        
        
        first_name = UserProfile.objects.filter(first_name__contains= search_post)
        
        return render(request, 'friend.html', {'posts': first_name})
        
    else:
        posts = UserProfile.objects.all().order_by("-born_date")
        return render(request, 'friend.html', {'posts': posts})
    
def allMessages(request):
    user=request.user.userprofile
    
    chats = ChatMessage.objects.all()
    message=ChatMessage.objects.filter(msg_sender=user)
    message2=ChatMessage.objects.filter(msg_receiver=user)
    print(message)
    print(message2)
    if message or message2:
        context={'chats':message,'chats2':message2,'user':user}
        return render(request,'allmessages.html',context)
    else:
        return render(request,'allmessages.html')
    


def exercise_delete(request,id):
   message=ChatMessage.objects.get(id=id)
   message.delete()

   return redirect('message')

def get_unreadMessage(request):
    user = request.user.userprofile
    
    
    
    chats = ChatMessage.objects.all()
    rec_chats = ChatMessage.objects.filter(seen=False)
    if rec_chats:
        context={'chats':rec_chats}
        return render(request,'unread.html',context)
    return render(request,'unread.html')
