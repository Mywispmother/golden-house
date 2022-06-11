from django.db import models
from django.contrib.auth.models import User


class Flat(models.Model):
    район_выбор= (
        ('Центр','Центр'),
        ('Южный','Южный'),
        ('Западный', 'Западный'),
        ('Северный', 'Северный'),
        ('Восточный', 'Восточный'),
    )
    Фото = models.ImageField('Фото',upload_to='')
    Фото1 = models.ImageField('Фото',upload_to='',null=True,blank=True)
    Фото2 = models.ImageField('Фото',upload_to='',null=True,blank=True)
    Фото3 = models.ImageField('Фото',upload_to='',null=True,blank=True )
    Адрес = models.TextField()
    Район = models.CharField(max_length=20,choices=район_выбор,null=True,blank=True)
    Дом = models.PositiveIntegerField()
    Подъезд = models.PositiveIntegerField()
    Этаж = models.IntegerField()
    Квартира = models.PositiveIntegerField()
    Комнат = models.PositiveIntegerField()
    Цена = models.PositiveIntegerField()
    Цена_наруки = models.PositiveIntegerField(null=True)
    Телефон = models.TextField(max_length=40,null=True,blank=True)
    Описание = models.TextField()
    Date = models.DateField(auto_now_add=True,null=True,blank=True)
    Updated = models.DateField(auto_now=True,null=True,blank=True)
    user = models.ForeignKey(to=User,
                             on_delete=models.SET_NULL,editable=False,null=True,blank=True)


    def __str__(self):
        return self.Адрес

