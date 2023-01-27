from django.db import models

# Create your models here.
class cartel(models.Model):
    name=models.CharField(unique=False,null=False,blank=False,max_length=100)
    price=models.IntegerField(unique=False,null=False,blank=False)
    description=models.CharField(unique=False,blank=False,null=False,max_length=100)
    slug=models.SlugField(unique=False,null=False,blank=False,max_length=100)
    def _str_(self) -> str:
        return self.name