# Generated by Django 3.2.5 on 2021-07-13 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='type',
            field=models.CharField(max_length=20),
        ),
    ]
