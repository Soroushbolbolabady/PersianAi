from django.db import models
from django.contrib.auth.models import User
from .services import main


# Create your models here.


class AiData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    to_ai = models.TextField()
    from_ai = models.TextField()

    def save(self , *args , **kwargs):
        self.from_ai = main(self.to_ai)
        super(AiData, self).save(*args,**kwargs)
