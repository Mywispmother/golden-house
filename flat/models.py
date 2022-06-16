from django.db import models
from django.contrib.auth.models import User

ТИП_ПРЕДЛОЖЕНИЯ = (
    ("Собственник", "Собственник"),
    ("Посредник", "Посредник"),
)
ТИП_ДОМА = (
    ('Дом', 'Дом'),
    ('Пол дома', 'Пол дома'),
    ('Квартира', 'Квартира'),
    ('Участок', 'Участок'),

)


class Flat(models.Model):
    район_выбор = (
        ('Центр', 'Центр'),
        ('Южный', 'Южный'),
        ('Западный', 'Западный'),
        ('Северный', 'Северный'),
        ('Восточный', 'Восточный'),
    )
    Фото = models.ImageField('Фото', upload_to='')
    Фото1 = models.ImageField('Фото', upload_to='', null=True, blank=True)
    Фото2 = models.ImageField('Фото', upload_to='', null=True, blank=True)
    Фото3 = models.ImageField('Фото', upload_to='', null=True, blank=True)
    Фото4 = models.ImageField('Фото', upload_to='', null=True, blank=True)
    Фото5 = models.ImageField('Фото', upload_to='', null=True, blank=True)
    Фото6 = models.ImageField('Фото', upload_to='', null=True, blank=True)
    Фото7 = models.ImageField('Фото', upload_to='', null=True, blank=True)
    Адрес = models.TextField()
    Район = models.CharField(max_length=20, choices=район_выбор, null=True, blank=True)
    Тип = models.CharField('Тип предложения', max_length=20, choices=ТИП_ПРЕДЛОЖЕНИЯ, null=True, blank=True)
    Тип_дома = models.CharField(max_length=20,choices=ТИП_ДОМА,null=True,blank=True )
    Дом = models.PositiveIntegerField()
    Подъезд = models.PositiveIntegerField()
    Этаж = models.IntegerField()
    Квартира = models.PositiveIntegerField()
    Комнат = models.PositiveIntegerField()
    Цена = models.PositiveIntegerField()
    Цена_наруки = models.PositiveIntegerField(null=True)
    Телефон = models.TextField(max_length=40, null=True, blank=True)
    Телефон_Соб = models.TextField('Телефон Собственика', max_length=40, null=True, blank=True)
    Описание = models.TextField()
    Date = models.DateField(auto_now_add=True, null=True, blank=True)
    Updated = models.DateField(auto_now=True, null=True, blank=True)
    Сотрудники = models.ForeignKey(to=User,
                                   on_delete=models.SET_NULL, editable=False, null=True, blank=True)

    def __str__(self):
        return self.Адрес
