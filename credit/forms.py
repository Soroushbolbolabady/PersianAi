from django.forms import ModelForm
from .models import UserCredit



class IncreaseCreditForm(ModelForm):

	class Meta:
		model = UserCredit
		fields = ('amount_credit',)