# Generated by Django 3.2.11 on 2022-01-25 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название города')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название улицы')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.city', verbose_name='Город')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название магазина')),
                ('opened', models.BooleanField(blank=True, default=False, verbose_name='Открыто')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.city', verbose_name='Город')),
                ('street', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.street', verbose_name='Улица')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
