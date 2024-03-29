# Generated by Django 5.0 on 2023-12-14 07:52

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UserAction",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user_action", models.CharField(max_length=50)),
                ("datetime", models.DateTimeField()),
                ("image_path", models.CharField(max_length=100)),
                ("user_id", models.IntegerField()),
                ("product_id", models.IntegerField()),
            ],
        ),
    ]
