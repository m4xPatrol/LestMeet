from django.db import models
from django.contrib.auth import get_user_model
user = get_user_model()


class EventClass(models.Model):
    categories = (
        (1, 'Развлечение'),
        (2, 'Спорт'),
        (3, 'Авто/Мото'),
        (4, 'Конференции'),
        (5, 'Мероприятия'),
        (6, 'Другое'),
    )
    pay_variants = (
        (1, 'Я'),
        (2, 'Вы'),
        (3, 'Пополам'),
    )

    id = models.IntegerField(primary_key=True)
    heading = models.CharField(verbose_name='Название', max_length=300, null=False)
    image = models.ImageField(verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание')
    category = models.IntegerField(verbose_name='Категория', choices=categories)
    pay = models.IntegerField(verbose_name='Кто платит', choices=pay_variants)
    user = models.ForeignKey(user, verbose_name='Пользователь', on_delete=models.CASCADE)
