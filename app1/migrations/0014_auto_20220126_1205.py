# Generated by Django 3.2.11 on 2022-01-26 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0013_alter_city_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=255, verbose_name='Название улицы')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.city')),
            ],
        ),
        migrations.AlterField(
            model_name='shop',
            name='street',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.street'),
        ),
    ]
