# Generated by Django 5.1.1 on 2024-10-02 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('networks', '0011_alter_switch_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='rack',
            name='colour',
            field=models.CharField(blank=True, choices=[('primary', 'primary'), ('secondary', 'secondary'), ('danger', 'danger'), ('info', 'info'), ('success', 'success'), ('warning', 'warning'), ('light', 'light'), ('dark', 'dark'), ('white', 'white')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='stack',
            name='colour',
            field=models.CharField(blank=True, choices=[('primary', 'primary'), ('secondary', 'secondary'), ('danger', 'danger'), ('info', 'info'), ('success', 'success'), ('warning', 'warning'), ('light', 'light'), ('dark', 'dark'), ('white', 'white')], max_length=100, null=True),
        ),
    ]
