from django.db import models
from django.contrib.auth.models import User


class PasswordEntry(models.Model):
    service_name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=30)
    email = models.EmailField(verbose_name='email', max_length=50)
    password = models.CharField(max_length=30)    
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}: {self.service_name}"
