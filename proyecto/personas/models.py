from django.db import models

# Create your models here.

class Domicilio(models.Model):
    calle = models.CharField(max_length=250)
    no_calle = models.CharField(max_length=250)
    pais = models.CharField(max_length=250) 

    def __str__(self) -> str:
        return f'Domicilio: Calle= {self.calle} , no_calle= {self.no_calle} , pais={self.pais}'



class Persona(models.Model):
    nombre= models.CharField(max_length=255)
    apellido= models.CharField(max_length =255)
    email= models.CharField(max_length=255)
    domicilio = models.ForeignKey(Domicilio, on_delete =models.CASCADE) #relacion 
    def __str__(self) -> str:
        return f'Persona: Id ={self.id},  Nombre= {self.nombre}, Apellido= {self.apellido}, Email={self.email}'