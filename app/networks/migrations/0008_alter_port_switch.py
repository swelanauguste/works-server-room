# Generated by Django 5.1.1 on 2024-09-24 17:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('networks', '0007_port_stack_alter_port_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='port',
            name='switch',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='networks.switch'),
        ),
    ]
