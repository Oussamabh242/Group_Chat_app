from email import message
import django
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Group , Message
from .forms import MessageForm
from django.utils import timezone 
import pytz
from django.contrib.auth.models import User

# Create your views here.
def all(request) : 

    groups = Group.objects.all()
    ing = []
    for group in groups : 
        if str(request.user) in group.get_members() : 
            ing.append(group) 
    context = {"g" : ing} 
    return render(request , "all.html" , context)

@login_required
def join(request) :

    print(request.user) 
    if request.method == "POST" : 
        Gid = request.POST.get("id" , False)
        if int(Gid)>0 and int(Gid)<= len(list(Group.objects.all())) : 
            Group.objects.get(id = Gid).members.add(request.user)
            return redirect("all")

    return render(request , "join.html" )

def myGroups(request) : 
    groups = Group.objects.all()
    ing = []
    for group in groups : 
        if request.user in group.get_members() : 
            ing.append(group) 
    context = {"g" : ing} 
    return render(request , "wtf.html" , context)

def single(request , pk) : 
    
    msg = Message.objects.filter(group=Group.objects.get(id=pk))
    msg_form= MessageForm(request.POST or None)
    if request.method=="POST ": 
        msg_form = MessageForm(request.POST)
        if msg_form.is_valid() : 
            msg_form.save() 
            return redirect('all')
    context = {
        "msg" : msg , 
        "form" : msg_form
    } 
    return render(request , "single.html" ,context)