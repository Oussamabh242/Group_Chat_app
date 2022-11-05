from django.shortcuts import render

# Create your views here.
def wellcome(request) : 
    return render(request , "wellcome.html")