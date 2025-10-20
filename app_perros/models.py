from django.db import models

class Perro(models.Model):
    
    id_perro = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name="Nombre del Perro")
    raza = models.CharField(max_length=100, verbose_name="Raza")
    fecha_nacimiento = models.DateField(blank=True, null=True, verbose_name="Fecha de Nacimiento")
    descripcion = models.TextField(blank=True, verbose_name="Descripción Adicional")

    class Meta:
        verbose_name = "Perro"
        verbose_name_plural = "Perros"

    def __str__(self):
        """
        Devuelve una representación de cadena del objeto Perro.
        """
        return f"{self.nombre} ({self.raza})"