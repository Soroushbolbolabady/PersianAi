from django.db import models
from accounts.models import CustomUser
from .services import main


# Create your models here.


class AiData(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    to_ai = models.TextField()
    from_ai = models.TextField()

    def save(self , *args , **kwargs):
        self.from_ai = main(self.to_ai)
        super(AiData, self).save(*args,**kwargs)
    
