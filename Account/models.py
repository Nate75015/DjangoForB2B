from django.db import models

# Create your models here.

class Account(models.Model):
    mail = models.EmailField(max_length=254)
    password = models.CharField(max_length=255)
    statut = models.IntegerField()

    def __str__(self):
        return "{} - {} - {} ".format(self.mail, self.password, self.statut)
