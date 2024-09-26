# Generated by Django 5.1.1 on 2024-09-24 16:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('networks', '0003_alter_port_network_alter_port_vlan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='port',
            name='network',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='networks.network'),
        ),
    ]
