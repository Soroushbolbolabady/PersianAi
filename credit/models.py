from django.db import models
from accounts.models import CustomUser

# Create your models here.


class UserCredit(models.Model):
	user = models.OneToOneField(CustomUser , on_delete=models.CASCADE)
	amount_credit = models.PositiveIntegerField(default = 0)


		



