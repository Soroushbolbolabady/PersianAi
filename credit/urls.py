from django.urls import path
from .views import show_user_credit



app_name = 'credit'


urlpatterns = [
	path('', show_user_credit , name = 'show_user_credit')
]