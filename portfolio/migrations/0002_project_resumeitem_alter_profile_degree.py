# Generated by Django 4.1.4 on 2022-12-12 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Project",
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
                ("title", models.CharField(max_length=32)),
                ("link", models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name="ResumeItem",
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
                ("title", models.CharField(max_length=32)),
                ("subtitle", models.CharField(max_length=32)),
                ("period", models.CharField(max_length=32)),
                ("description", models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name="profile",
            name="degree",
            field=models.CharField(max_length=32),
        ),
    ]