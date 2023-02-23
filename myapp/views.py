from django.shortcuts import render
from .models import *

# Create your views here.
def Home(request):
    return render(request,"app/home.html")
def About(request):
    return render(request,"app/about.html")
def Project(request):
    return render(request,"app/project.html")
def Contact(request):
    if request.method=="POST":
       name=request.POST['name']   
       email=request.POST['email']   
       phone=request.POST['phone']   
       concern=request.POST['concern']  
        
       obj=ContactMe(Name=name,Email=email,Phone=phone,Concern=concern)
       obj.save()  
    return render(request,"app/contact.html")

def Resume(request):
    return render(request,"app/resume.html")
def ProjectList(request):
    return render(request,"app/projectlist.html")
    


