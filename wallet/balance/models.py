from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Signup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.IntegerField()

    def __str__(self):
        return self.user.username+" "+str(self.balance)

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField()
    cr_dr = models.CharField(max_length=40)

    def __str__(self):
        return self.user.username+" "+str(self.amount)
