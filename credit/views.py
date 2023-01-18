from django.shortcuts import render
from .models import UserCredit

# Create your views here.


def show_user_credit(request , user_id):
	credit =  UserCredit.objects.get(user = user_id)
	context = {
		'user' : user_id
	}
	return render(request , 'credit/show_user_credit.html' , context)