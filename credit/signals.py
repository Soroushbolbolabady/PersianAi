from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import UserCredit
from accounts.models import CustomUser




@receiver(post_save , sender = CustomUser)
def credit_post_save(sender , instance , created , *args , **kwargs):
	if created:
		UserCredit.objects.create(user = instance)