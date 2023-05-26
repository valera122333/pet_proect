from django.db import models
from django.db.models import *
import datetime
from django.contrib.auth.models import User
# from django.db.models.fields.files import ImageField
# Create your models here.

class Pet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    title = models.CharField(max_length=40,verbose_name='Кличка')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(verbose_name='Изображение животного',upload_to='pets/images')
    data = models.DateField(verbose_name='День рождение питомца')

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Животные'