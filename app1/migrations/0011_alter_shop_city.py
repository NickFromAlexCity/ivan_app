# Generated by Django 3.2.11 on 2022-01-25 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_rename_shopmodel_shop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.city'),
        ),
    ]
