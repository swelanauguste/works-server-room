# Generated by Django 5.1.1 on 2024-10-02 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('networks', '0010_switch_sort'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='switch',
            options={'ordering': ['sort'], 'verbose_name_plural': 'switches'},
        ),
    ]
