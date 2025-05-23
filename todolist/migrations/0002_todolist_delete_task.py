# Generated by Django 5.2 on 2025-04-20 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todolist", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Todolist",
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
                ("text", models.CharField(max_length=45)),
                ("completed", models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name="Task",
        ),
    ]
