from django.db import models

# Create your models here.

class Spent(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True)
    price = models.BigIntegerField(null=True, blank=True)
    type = models.CharField(max_length=256, null=True, blank=True)
    time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return str(self.type)
