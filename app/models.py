from django.db import models
from django.contrib.auth.models import User

class Interest(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    mobile_number = models.CharField(max_length=15, default='') 
    whatsapp_number = models.CharField(max_length=15, blank=True, null=True)
    interests = models.ManyToManyField(Interest, blank=True)

    def __str__(self):
        return self.user.username

