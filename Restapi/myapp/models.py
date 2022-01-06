from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Detail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='address')
    adress = models.TextField(max_length=500, blank=False)
    