# Generated by Django 3.1.2 on 2021-08-10 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reclamos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reclamo',
            name='consulta',
            field=models.TextField(max_length=300),
        ),
    ]
