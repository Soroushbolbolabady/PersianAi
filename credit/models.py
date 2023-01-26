from django.db import models
from accounts.models import CustomUser
# Create your models here.


class UserCredit(models.Model):
	user = models.ForeignKey(CustomUser , on_delete=models.CASCADE)
	amout_credit = models.PositiveIntegerField(default = 0)


	def __str__(self):
		return self.amout_credit

		