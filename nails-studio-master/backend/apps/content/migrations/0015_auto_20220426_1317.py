# Generated by Django 3.2.10 on 2022-04-26 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0014_comment_course'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-date_created'], 'verbose_name': 'Сообщение', 'verbose_name_plural': 'Сообщения'},
        ),
        migrations.RemoveField(
            model_name='comment',
            name='is_published_landing',
        ),
        migrations.AlterField(
            model_name='comment',
            name='category',
            field=models.IntegerField(choices=[(0, 'Сообщение'), (1, 'Курсы')], default=0, verbose_name='Категория сообщения'),
        ),
    ]
