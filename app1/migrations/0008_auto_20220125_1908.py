# Generated by Django 3.2.11 on 2022-01-25 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_auto_20220125_1835'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='streetmodel',
            name='city',
        ),
        migrations.AlterModelOptions(
            name='shopmodel',
            options={},
        ),
        migrations.DeleteModel(
            name='CityModel',
        ),
        migrations.DeleteModel(
            name='StreetModel',
        ),
    ]