# Generated by Django 3.0.6 on 2020-06-14 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('items_json', models.CharField(max_length=100000)),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('mobile', models.CharField(max_length=20)),
                ('whatsapp', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('address1', models.CharField(max_length=400)),
                ('address2', models.CharField(max_length=400)),
                ('zip_code', models.CharField(max_length=20)),
            ],
        ),
    ]
