# Generated by Django 3.2.12 on 2022-07-15 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortner', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='uuid',
            field=models.CharField(max_length=10),
        ),
    ]
