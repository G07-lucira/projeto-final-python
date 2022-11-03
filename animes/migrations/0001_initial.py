# Generated by Django 4.1.2 on 2022-11-03 17:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("genres", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Anime",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=127)),
                ("total_eps", models.PositiveIntegerField()),
                ("anime_img", models.CharField(max_length=127)),
                ("synopsis", models.TextField()),
                ("author", models.CharField(max_length=127)),
                ("release_date", models.PositiveIntegerField()),
                ("is_finished", models.BooleanField()),
                (
                    "genres",
                    models.ManyToManyField(related_name="animes", to="genres.genre"),
                ),
            ],
        ),
    ]
