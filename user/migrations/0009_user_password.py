# Generated by Django 5.1.2 on 2024-11-05 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_remove_payment_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default=models.CharField(max_length=11, unique=True), max_length=128),
        ),
    ]
