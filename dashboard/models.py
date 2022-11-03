from django.db import models

# Create your models here.
CATEGORY = (
    ('Cesarea', 'Cesarea'),
    ('Parto natural', 'Parto natural'),
)

CATEGORY1 = (
    ('Pobreza heredada', 'Pobreza heredada'),
    ('Banca rota', 'Banca rota'),
    ('Sin trabajo', 'Sin trabajo'),
)

CATEGORY2 = (
    ('ICETEX', 'ICETEX'),
    ('Pago de matricula', 'Pago de matricula'),
    ('Becados', 'Becados'),
)

class Elementos(models.Model):
    Year = models.CharField(max_length=100, null=True)
    Cantidad = models.PositiveIntegerField(null=True)
    Categoria = models.CharField(max_length=50, choices=CATEGORY, null=True)

    def __str__(self):
        return f'{self.Year}'
    
class Elementos1(models.Model):
    Year = models.CharField(max_length=100, null=True)
    Cantidad = models.PositiveIntegerField(null=True)
    Categoria = models.CharField(max_length=50, choices=CATEGORY1, null=True)

    def __str__(self):
        return f'{self.Year}'
    
class Elementos2(models.Model):
    Year = models.CharField(max_length=100, null=True)
    Cantidad = models.PositiveIntegerField(null=True)
    Categoria = models.CharField(max_length=50, choices=CATEGORY2, null=True)

    def __str__(self):
        return f'{self.Year}'
