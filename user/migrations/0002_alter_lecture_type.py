# Generated by Django 5.1.2 on 2024-10-31 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='type',
            field=models.CharField(choices=[('Musculação', 'Musculação'), ('Fisioterapia', 'Fisioterapia'), ('CrossFit', 'CrossFit'), ('Gap', 'Gap')], max_length=40),
        ),
    ]
