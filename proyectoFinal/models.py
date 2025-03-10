from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    state = models.CharField(
        max_length=20,
        choices=[
            ('por_realizar', 'Por Realizar'),
            ('en_transito', 'En Transito'),
            ('completada', 'Completada')
        ],
        default='por_realizar'
    )