# Generated by Django 4.2.10 on 2024-03-02 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_task_frequency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='frequency',
            field=models.CharField(choices=[('hourly', 'Hourly'), ('weekly', 'Weekly'), ('every_1m', 'Every min'), ('yearly', 'Yearly'), ('every_30m', 'Every 30 min'), ('every_10m', 'Every 10 min')], default='hourly', max_length=10),
        ),
    ]