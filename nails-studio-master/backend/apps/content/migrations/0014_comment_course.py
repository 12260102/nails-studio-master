# Generated by Django 3.2.10 on 2022-04-26 01:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0013_comment_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='content.course', verbose_name='Курс'),
        ),
    ]
