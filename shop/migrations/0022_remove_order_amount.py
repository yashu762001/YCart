# Generated by Django 3.0.6 on 2020-06-16 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0021_auto_20200616_1649'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='amount',
        ),
    ]