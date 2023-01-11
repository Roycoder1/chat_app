
from django import forms
from django.forms import ModelForm
from .models import ChatMessage,UserProfile,Friend


class ChatMessageForm(ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={"class":"forms", "rows":3, "placeholder": "Type message here"}))
    subject=forms.CharField(max_length=300)

    class Meta:
        model = ChatMessage

        fields = '__all__'
        exclude=['msg_sender','msg_receiver','seen']

class UserProfilForm(forms.ModelForm):
    
    class Meta:
        model = UserProfile
        fields = '__all__' 
        exclude = ['user','friends']
        widgets = {
            # 'first_name': forms.CharField(widget=forms.CharField(max_length=300)),
            # 'last_name': forms.CharField(widget=forms.CharField(max_length=300)),
            
            'born_date': forms.DateTimeInput(attrs={'type' : 'date', 'class':'date'}),
            'email': forms.EmailInput(attrs={'class' : 'mail'}),
            'phone_number': forms.NumberInput(attrs={'class' : 'phone'}),
            'age':forms.NumberInput(attrs={'class' : 'age'}),
            
        }

class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = '__all__' 
        exclude=['profile']