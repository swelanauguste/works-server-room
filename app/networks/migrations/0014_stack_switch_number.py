# Generated by Django 5.1.1 on 2024-10-11 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('networks', '0013_port_is_critical'),
    ]

    operations = [
        migrations.AddField(
            model_name='stack',
            name='switch_number',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
