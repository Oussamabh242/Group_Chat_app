from pickle import FALSE
from django.shortcuts import redirect, render , HttpResponse   
from django.contrib.auth import login , authenticate
from .forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm
import django



# Create your views here.


def login1(request) : 
        # if request.method=="POST" : 
        #     form = AuthenticationForm(request , data=request.POST)
        #     if form.is_valid() :
        #         user= form.get_user()
        #         django.contrib.auth.login(request , user)
        #         return redirect("signup")
        # else : 
        #     form = AuthenticationForm(request)
        # return render(request , "h.html" , {"form" : form})
        username= request.POST.get('u' , False)
        print(username)
        return render(request , 'h.html')

def login(request) : 
    if request.method == "POST" : 
        username = request.POST.get('u' , False)
        password = request.POST.get("p" , False)
        user = authenticate(username= username , password = password)
        if user is not None : 
            django.contrib.auth.login(request , user)
            return redirect("all")
    return render(request , 'h.html')

def signup(request) : 
    print(request.user)
    if request.method == "POST" : 
        regform = NewUserForm(request.POST)
        if regform.is_valid() : 
            regform.save()
            return redirect("login")
    else: 
        regform = NewUserForm()
    return render(request, "signup.html" , {"regform" : regform})