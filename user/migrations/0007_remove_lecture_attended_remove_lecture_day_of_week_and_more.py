# Generated by Django 5.1.2 on 2024-11-01 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_lecture_attended_lecture_day_of_week_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecture',
            name='attended',
        ),
        migrations.RemoveField(
            model_name='lecture',
            name='day_of_week',
        ),
        migrations.RemoveField(
            model_name='lecture',
            name='days_before',
        ),
        migrations.RemoveField(
            model_name='lecture',
            name='months_as_member',
        ),
        migrations.RemoveField(
            model_name='lecture',
            name='time',
        ),
        migrations.RemoveField(
            model_name='lecture',
            name='weight',
        ),
        migrations.AddField(
            model_name='user',
            name='attended',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='day_of_week',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='days_before',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='months_as_member',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='time',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='weight',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]