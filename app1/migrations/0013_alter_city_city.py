# Generated by Django 3.2.11 on 2022-01-25 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0012_alter_city_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='city',
            field=models.CharField(max_length=255, verbose_name='Название города'),
        ),
    ]