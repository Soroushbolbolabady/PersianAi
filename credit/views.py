from django.shortcuts import render ,redirect
from .models import UserCredit
from accounts.models import CustomUser
from .forms import IncreaseCreditForm

# Create your views here.



def show_user_credit(request):
	if request.user.is_authenticated:
		user = CustomUser.objects.filter(email = request.user).values().get()
		user_id = user['id']
		credit =  UserCredit.objects.filter(user_id = user_id).get()
		context = {
			'user_credit' : credit
		}
		return render(request , 'credit/show_user_credit.html' , context)


def increase_user_credit(request):
	if request.user.is_authenticated:
		user = request.user.usercredit
		if request.method == 'POST':
			form = IncreaseCreditForm(request.POST ,instance=user)
			if form.is_valid():
				form.save()
				
			return redirect('home:home')
		else:
			form = IncreaseCreditForm()
			context = {
				'form' : form
			}
			return render(request , 'credit/increase_user_credit.html' , context)

	

