# Generated by Django 3.0.3 on 2020-05-03 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0009_auto_20200503_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
