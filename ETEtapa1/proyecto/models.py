from django.db import models

class Proveedores(models.Model):
    NumeroIdentificacion = models.CharField ( max_length = 9 )
    NombreProveedor = models.CharField ( max_length = 150 )
    TelefonoProveedor = models.IntegerField (  )
    DireccionProveedor = models.CharField ( max_length = 200 )
    EmailProveedor = models.CharField ( max_length = 100 )
    PaisProveedor = models.CharField ( max_length = 20 )
    ContraseñaProveedor = models.CharField ( max_length = 90 )

def __str__(self):
    return self.NombreProveedor
