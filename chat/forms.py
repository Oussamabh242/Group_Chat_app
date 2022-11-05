from pyexpat import model
from django import forms
from .models import Message

class MessageForm(forms.Form) :
    class Meta : 
        model = Message
        fields = ["sender" ,"body",  "group" , "time"]
