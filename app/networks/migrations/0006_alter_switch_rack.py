# Generated by Django 5.1.1 on 2024-10-02 00:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('networks', '0005_switch_serial_number_alter_switch_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='switch',
            name='rack',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='racks', to='networks.rack'),
        ),
    ]
