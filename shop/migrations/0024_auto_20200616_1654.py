# Generated by Django 3.0.6 on 2020-06-16 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0023_order_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='amount',
        ),
        migrations.AddField(
            model_name='order',
            name='value',
            field=models.IntegerField(default=0),
        ),
    ]
