# Generated by Django 3.2.5 on 2021-07-16 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_management', '0003_property_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='description',
            field=models.TextField(),
        ),
    ]
