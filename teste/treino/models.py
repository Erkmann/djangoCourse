from django.db import models

class Numeros(models.Model):
    numero = models.IntegerField()

    def __str__(self):
        return self.numero
