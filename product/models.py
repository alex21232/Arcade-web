from django.db import models
from django.contrib.auth.models import User

class Juego(models.Model):  # Cambiado nombre de clase
    # Información básica del juego
    nombre = models.CharField(
        max_length=200, 
        verbose_name="Nombre del juego",
        help_text="Ej: The Legend of Zelda: Breath of the Wild"
    )
    
    # Plataforma y detalles
    PLATAFORMAS = [
        ('PC', 'PC'),
        ('PS5', 'PlayStation 5'),
        ('PS4', 'PlayStation 4'),
        ('XBOX_SERIES', 'Xbox Series X/S'),
        ('XBOX_ONE', 'Xbox One'),
        ('SWITCH', 'Nintendo Switch'),
        ('MOBILE', 'Mobile'),
        ('OTHER', 'Otra plataforma'),
    ]
    
    plataforma = models.CharField(
        max_length=20,
        choices=PLATAFORMAS,
        verbose_name="Plataforma"
    )
    
    # Géneros disponibles
    GENEROS = [
        ('ACCION', 'Acción'),
        ('AVENTURA', 'Aventura'),
        ('RPG', 'RPG'),
        ('DEPORTES', 'Deportes'),
        ('CARRERAS', 'Carreras'),
        ('ESTRATEGIA', 'Estrategia'),
        ('SHOOTER', 'Shooter'),
        ('SIMULACION', 'Simulación'),
        ('INDIE', 'Indie'),
        ('OTRO', 'Otro'),
    ]
    
    genero = models.CharField(
        max_length=20,
        choices=GENEROS,
        verbose_name="Género"
    )
    
    # Estado del juego
    ESTADOS = [
        ('NUEVO', 'Nuevo - Sellado'),
        ('USADO_EXCELENTE', 'Usado - Excelente estado'),
        ('USADO_BUENO', 'Usado - Buen estado'),
        ('USADO_REGULAR', 'Usado - Estado regular'),
        ('SIN_CAJA', 'Sin caja'),
    ]
    
    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        verbose_name="Estado del juego",
        default='USADO_BUENO'
    )
    
    desarrollador = models.CharField(
        max_length=100,
        verbose_name="Desarrollador",
        help_text="Ej: Nintendo, Sony, Microsoft, etc."
    )
    
    año_lanzamiento = models.PositiveIntegerField(
        verbose_name="Año de lanzamiento",
        help_text="Ej: 2023"
    )
    
    # Descripción breve
    descripcion = models.TextField(
        max_length=500,
        verbose_name="Descripción",
        help_text="Describe el estado, contenido, si tiene manuales, etc."
    )
    
    # Precio
    precio = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name="Precio ($)"
    )
    
    # Imagen
    imagen = models.ImageField(
        upload_to='juegos/',  # Cambiada la carpeta
        verbose_name="Imagen del juego",
        help_text="Sube una foto clara del juego"
    )
    
    # Fechas automáticas
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    # Estado del anuncio
    publicado = models.BooleanField(default=True, verbose_name="Publicado")
    vendido = models.BooleanField(default=False, verbose_name="Vendido")
    
    class Meta:
        verbose_name = "Juego"  # Cambiado
        verbose_name_plural = "Juegos"  # Cambiado
        ordering = ['-fecha_creacion']
    
    def __str__(self):
        return f"{self.nombre} - {self.get_plataforma_display()} (${self.precio})"