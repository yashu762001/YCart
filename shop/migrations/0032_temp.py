# Generated by Django 3.0.6 on 2020-06-16 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0031_remove_order_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='temp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coro', models.CharField(max_length=23)),
            ],
        ),
    ]
