# Generated by Django 3.2.15 on 2022-09-13 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='server_address',
            field=models.GenericIPAddressField(unpack_ipv4=True),
        ),
    ]
