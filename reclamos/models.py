import uuid

from django.contrib.auth.models import User
from django.urls import reverse

from django.db import models


class Categoria(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=150, unique=True, verbose_name='Categoria')

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('categoria_list', args=[str(self.id)])

    class Meta:
        verbose_name_plural= 'Categorias'


def seguimiento():
    codigo =str(uuid.uuid4())

    return (codigo[:10])

class Reclamo(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    ESTADO_OPCIONES = (
        ('PENDIENTE', 'Pendiente'),
        ('EN PROCESO', 'En proceso'),
        ('CERRADO', 'Cerrado'),
    )

    tiket = models.CharField(max_length=20, default=seguimiento,)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.IntegerField(verbose_name='DNI')
    carrera = models.CharField(max_length=150,)
    registro = models.BigIntegerField(blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name='Asunto')
    fecha_creada = models.DateTimeField(auto_now_add=True)
    fecha_modificada = models.DateTimeField(auto_now=True)
    email = models.EmailField()
    telefono = models.BigIntegerField(blank=True, null=True)
    estado = models.CharField(choices=ESTADO_OPCIONES, default='PENDIENTE', max_length=100)
    consulta = models.TextField(max_length=300)

    def __str__(self):
        return self.tiket

    def get_absolute_url(self):
        return reverse('consulta_estado', args=[str(self.id)])

    def save(self, **kwargs):
        self.tiket = self.tiket.upper()
        super(Reclamo, self).save()

    class Meta:
        verbose_name_plural='Reclamos'
        ordering=('fecha_creada',)
        permissions = (
            ('ver_examen', 'Ver Examen'),
            ('ver_cursada', 'Ver Cursada'),
            ('ver_ingreso', 'Ver Ingreso'),
            ('ver_mayores_25', 'Ver Ingreso Mayores de 25'),
            ('ver_equivalencia', 'Ver Equivalcencia'),
            ('ver_programas_planes', 'Ver Certificacion de programas y planes'),
            ('ver_egreso', 'Ver Egreso'),
            ('ver_trabajo_final', 'Ver Trabajo Final'),
            ('ver_alumno_vocacional', 'Ver alumno vocacional'),
            ('ver_cambio_plan', 'Ver cambio de plan'),
            ('admin', 'Administrador'),
            ('empleado', 'Empleado')
        )

class Respuesta(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    reclamo = models.ForeignKey(Reclamo, on_delete=models.CASCADE)
    fecha_respuesta=models.DateTimeField(auto_now_add=True)
    respuesta= models.TextField()

    def __str__(self):
        return str(self.reclamo.categoria)

    class Meta:
        verbose_name_plural= 'Respuestas'