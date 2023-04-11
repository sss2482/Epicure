from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, SetPasswordForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Create your forms here.

class NewUserForm(UserCreationForm):
	class Meta:
		model = get_user_model()
		fields = ("username", "email", "password1", "password2")

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email / Username')

from django.contrib.auth.forms import SetPasswordForm
...
class SetPasswordForm(SetPasswordForm):
    class Meta:
        model = get_user_model()
        fields = ['new_password1', 'new_password2']