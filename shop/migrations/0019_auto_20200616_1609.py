# Generated by Django 3.0.6 on 2020-06-16 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0018_auto_20200616_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderupdate',
            name='update_desc',
            field=models.CharField(max_length=5000),
        ),
    ]
