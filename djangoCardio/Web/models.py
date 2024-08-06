from django.db import models

# Create your models here.
edad = models.IntegerField()
genero = models.BooleanField()
talla = models.FloatField()
peso = models.FloatField()
sistolica = models.FloatField()
diastolica = models.FloatField()
colesterol = models.FloatField()
glucosa = models.FloatField()
fuma = models.BooleanField()
bebe_alcohol = models.BooleanField()
practica_deporte = models.BooleanField()
imc = models.FloatField(blank=True, null=True)

# age
# gender
# height
# weight
# ap_hi
# ap_lo
# cholesterol
# gluc
# smoke
# alco
# active
# cardio---
# bmi