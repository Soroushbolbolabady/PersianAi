from django.shortcuts import render , redirect
from .forms import CustomUserCreationForm , SignInForm
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
# Create your views here.



def sign_in(request):
	if not request.user.is_authenticated:
	
		if request.method == "POST":
			email = request.POST['email']
			password = request.POST['password']
			user = authenticate(request , email = email , password = password)
			if user is not None :
				login(request , user)
				messages.success(request , f'Welcome {email}')
				return redirect('home:home')
	
		else:
			form = SignInForm()
		context = {
			'form' : form
		}
		return render(request , 'accounts/sign_in.html',context)
	else:
		return redirect('home:home')

def sign_up(request):
	if not request.user.is_authenticated:

		if request.method == 'POST':
			form = CustomUserCreationForm(request.POST)
			if form.is_valid:
				user = form.save()
				login(request , user)
				return redirect('home:home')
		else:
			form = CustomUserCreationForm()
	
		context = {
			'form':form
		}
		return render(request , 'accounts/sign_up.html' , context)
	else:
		return redirect('home:home')

def sign_out(request):
	logout(request)
	return render(request , 'accounts/sign_out.html')
