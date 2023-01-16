from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from django.utils.translation import gettext_lazy as _
from django import forms
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
	class Meta:
		model = CustomUser
		fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

	class Meta:
		model = CustomUser
		fields = ('email',)



class SignInForm(forms.Form):

	email = forms.EmailField()
	password = forms.CharField(label= _('password') , widget = forms.PasswordInput)