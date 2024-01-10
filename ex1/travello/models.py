from django.db import models
# Create your models here.
class destination(models.Model):
    id:int
    name:str
    desc:str
    img:str
    price:str
    offer:bool
