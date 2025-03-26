from django.shortcuts import render
import random
#from django.http import HttpResponse

# Create your views here.
def about(request):
    return render(request,"generator/about.html")
    
    
def home(request):
    return render(request,"generator/home.html")


def password(request):
    
    charactaers = list('abcdefghijklmnñopqrstuvwxyz')
    generater_password = ""
    
    
    length = int(request.GET.get("length"))  
    
    if request.GET.get("uppsercase"):
        charactaers.extend(list("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"))
        
    if request.GET.get("special"):
        charactaers.extend(list('-_+!@#$%^&*()'))
    
    if request.GET.get("numbers"):
        charactaers.extend(list("0123456789"))
    
    for x in range(length):

        generater_password += random.choice(charactaers)
    
    return render(request,"generator/password.html",{'password': generater_password})

