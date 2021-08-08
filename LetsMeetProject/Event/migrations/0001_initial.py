# Generated by Django 3.2.6 on 2021-08-07 06:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EventClass',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('heading', models.CharField(max_length=300, verbose_name='Название')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('description', models.TextField(verbose_name='Описание')),
                ('category', models.IntegerField(choices=[(1, 'Развлечение'), (2, 'Спорт'), (3, 'Авто/Мото'), (4, 'Конференции'), (5, 'Мероприятия'), (6, 'Другое')], verbose_name='Категория')),
                ('pay', models.IntegerField(choices=[(1, 'Я'), (2, 'Вы'), (3, 'Пополам')], verbose_name='Кто платит')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
    ]
