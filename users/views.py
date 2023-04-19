from django.shortcuts import render
# from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
# Create your views here.

from .models import User

def signupv(request):
    if request.method=='POST':
        name= request.POST['name']
        phone_number= request.POST['number']
        email= request.POST['email']
        passward= request.POST['pass']
        phone_number=request.POST['number']
        user= User.objects.create_user(username=name,email=email, password=passward, phone_number=phone_number)
        user.save()

    

        return HttpResponseRedirect(reverse_lazy('Login'))
    return render(request, 'Signup.html')



def loginv(request):
    if request.method=='POST':
        email= request.POST['email']
        passw= request.POST['pass']
        try:
            user= User.objects.get(email=email)
        except:
            messages.info(request,'email is not registered.Please register')
            return HttpResponseRedirect(reverse_lazy('Login'))
        print(user.username)
        print(passw)
        if user != None:
            # username= user.username
            check=auth.authenticate(username=user, password=passw)
            if check!= None:
                auth.login(request, check)
                return HttpResponseRedirect(reverse_lazy('Mainpage'))
            else:
                messages.info(request, 'invalid passward')
                return HttpResponseRedirect(reverse_lazy('Login'))
    return render(request, 'index.html')
    
def logoutv(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse_lazy('Home'))
        