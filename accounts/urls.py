from django.urls import path
from .views import sign_in , sign_up , sign_out



app_name = 'accounts'


urlpatterns = [
	path('signin/' , sign_in , name = 'sign_in'),
	path('signup/', sign_up , name = 'sign_up'),
	path('signout/', sign_out, name = 'sign_out')
	]