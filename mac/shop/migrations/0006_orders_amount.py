# Generated by Django 4.1.7 on 2023-08-07 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0005_orderupdate"),
    ]

    operations = [
        migrations.AddField(
            model_name="orders",
            name="amount",
            field=models.IntegerField(default=0),
        ),
    ]
