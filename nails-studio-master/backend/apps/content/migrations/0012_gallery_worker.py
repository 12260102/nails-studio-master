# Generated by Django 3.2.9 on 2022-04-19 23:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0011_gallery'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='worker',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pictures', to='content.worker'),
        ),
    ]