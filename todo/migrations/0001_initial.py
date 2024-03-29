# Generated by Django 4.2.7 on 2024-03-01 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Task",
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
                ("text", models.TextField()),
                ("date", models.DateTimeField()),
                ("deadline", models.DateTimeField(null=True)),
                ("done", models.BooleanField(default=False)),
            ],
        ),
    ]
