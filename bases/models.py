from django.db import models
from django.contrib.auth.models import User

class ClaseModelo(models.Model):
    estado = models.BooleanField(default=True)
    fec_Crea = models.DateTimeField(auto_now_add=True)
    fec_Modi = models.DateTimeField(auto_now=True)
    Usu_Crea = models.ForeignKey(User, on_delete = models.CASCADE)
    Usu_Modi = models.IntegerField(blank = True, null = True)

    class Meta:
        abstract = True
        

