from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    dateofbirth = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.username

   