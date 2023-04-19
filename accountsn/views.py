
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User

from .forms import NewUserForm, LoginForm, SetPasswordForm

class sgnup(CreateView):
    form_class=NewUserForm
    template_name='signup.html'
    success_url=reverse_lazy('login')
    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)

def signup(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			auth.login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("mass_mail")
		messages.error(request, str(form.errors))
	form = NewUserForm()
	return render (request=request, template_name="signup.html", context={"signup_form":form})


def lgn(request):
    if request.method=='POST':
        email=request.POST['email']
        pword=request.POST['password']
        ch=auth.authenticate(username=email,password=pword)
        if ch is not None:
            auth.login(request,ch)
            return HttpResponseRedirect(reverse_lazy('mass_mail'))
        else:
            messages.info(request,'invalid username or password')
            return HttpResponseRedirect(reverse_lazy('login'))
    else:
        return render(request,'login.html')
def login(request):
    if request.method == "POST":
            form = LoginForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = auth.authenticate(username=username, password=password)
                if user is not None:
                    auth.login(request, user)
                    messages.info(request, f"You are now logged in as {username}.")
                    return redirect("mass_mail")
                else:
                    messages.error(request,"Invalid username or password.")
            else:
                messages.error(request,"Invalid username or password.")
    form = LoginForm()
    return render(request=request, template_name="login.html", context={"login_form":form})



def password_change(request):
    user = request.user
    if request.method == 'POST':
        form = SetPasswordForm(user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your password has been changed")
            return redirect('login')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    form = SetPasswordForm(user)
    return render(request, 'password_change.html', {'password_change_form': form})

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse_lazy('login'))