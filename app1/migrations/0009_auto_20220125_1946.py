# Generated by Django 3.2.11 on 2022-01-25 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_auto_20220125_1908'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=255, verbose_name='Название города')),
            ],
        ),
        migrations.AlterField(
            model_name='shopmodel',
            name='city',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app1.city'),
        ),
    ]
