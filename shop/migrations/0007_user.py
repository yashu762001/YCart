# Generated by Django 3.0.6 on 2020-05-27 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20200526_1202'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('username', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=60)),
                ('confirmpassword', models.CharField(max_length=60)),
                ('MobileNumber', models.IntegerField()),
                ('WhatsappNumber', models.IntegerField()),
                ('ResidenceAddress', models.CharField(max_length=60)),
                ('OtherAddress', models.CharField(max_length=60)),
            ],
        ),
    ]
