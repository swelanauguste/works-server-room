# Generated by Django 5.1.1 on 2024-09-26 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('networks', '0016_port_port'),
    ]

    operations = [
        migrations.AlterField(
            model_name='port',
            name='port',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
