# Generated by Django 5.1.2 on 2024-11-01 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_remove_user_matricula_remove_user_lecture_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='attended',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='lecture',
            name='day_of_week',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='lecture',
            name='days_before',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='lecture',
            name='months_as_member',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='lecture',
            name='time',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='lecture',
            name='weight',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]
