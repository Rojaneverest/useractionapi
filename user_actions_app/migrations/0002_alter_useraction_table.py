# Generated by Django 5.0 on 2023-12-14 10:24

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("user_actions_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="useraction",
            table="user_actions",
        ),
    ]
