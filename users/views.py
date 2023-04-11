from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
# Create your views here.

def signupv(request):
    if request.method=='POST':
        name= request.POST['name']
        phone_number= request.POST['number']
        email= request.POST['email']
        passward= request.POST['pass']
        user= User.objects.create_user(username=name,email=email, password=passward)
        user.save()
        return HttpResponseRedirect(reverse_lazy('Login'))
    return render(request, 'Signup.html')

def logn(request):
    if request.method=='POST':
        usn=request.POST['username']
        pword=request.POST['password']
        ch=auth.authenticate(username=usn,password=pword)
        if ch is not None:
            auth.login(request,ch)
            return HttpResponseRedirect(reverse_lazy('home'))
        else:
            messages.info(request,'invalid username or password')
            return HttpResponseRedirect(reverse_lazy('login'))
    else:
        return render(request,'registration/login.html')

def loginv(request):
    if request.method=='POST':
        email= request.POST['email']
        passw= request.POST['pass']
        user= User.objects.get(username=email)
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
        else:
            messages.info(request,'email is not registered.Please register')
            return HttpResponseRedirect(reverse_lazy('Login'))
    return render(request, 'index.html')
        

        