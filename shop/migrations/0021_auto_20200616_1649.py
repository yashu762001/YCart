# Generated by Django 3.0.6 on 2020-06-16 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0020_order_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='amount',
            field=models.IntegerField(default=0, max_length=100),
        ),
    ]