# Generated by Django 4.2.10 on 2024-02-27 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_task_frequency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='frequency',
            field=models.CharField(choices=[('every_1m', 'Every min'), ('weekly', 'Weekly'), ('yearly', 'Yearly'), ('hourly', 'Hourly'), ('every_10m', 'Every 10 min'), ('every_30m', 'Every 30 min')], default='hourly', max_length=10),
        ),
    ]