# Generated by Django 3.2.7 on 2023-05-31 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_alter_product_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='size',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
