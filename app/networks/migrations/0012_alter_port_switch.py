# Generated by Django 5.1.1 on 2024-09-24 23:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('networks', '0011_alter_switch_stack'),
    ]

    operations = [
        migrations.AlterField(
            model_name='port',
            name='switch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ports', to='networks.switch'),
        ),
    ]
