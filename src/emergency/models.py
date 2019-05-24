from django.db import models
from django.conf import settings
# Create your models here.

class Emergency(models.Model):
    admin=models.ForeignKey(settings.AUTH_USER_MODEL)
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    def __str__(self):
        return str(self.id)


class Alert(models.Model):
	admin=models.ForeignKey(settings.AUTH_USER_MODEL)
	location=models.CharField(max_length=100)

  