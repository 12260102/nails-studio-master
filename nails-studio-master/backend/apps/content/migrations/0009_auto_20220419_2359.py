# Generated by Django 3.2.9 on 2022-04-19 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0008_course_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['order'], 'verbose_name': 'Курс', 'verbose_name_plural': 'Курсы'},
        ),
        migrations.AlterModelOptions(
            name='offerslide',
            options={'ordering': ['order'], 'verbose_name': 'Слайд предложения', 'verbose_name_plural': 'Слайды предложений'},
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ['order'], 'verbose_name': 'Услуга', 'verbose_name_plural': 'Услуги'},
        ),
        migrations.AddField(
            model_name='comment',
            name='phone',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(blank=True, null=True, verbose_name='Отзыв'),
        ),
    ]