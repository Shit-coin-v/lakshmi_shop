# Generated by Django 3.2.7 on 2023-05-31 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20230531_0650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.PositiveIntegerField(default=0),
        ),
    ]