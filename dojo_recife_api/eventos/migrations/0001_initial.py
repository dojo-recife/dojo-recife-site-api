# Generated by Django 4.1.7 on 2023-04-02 02:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Evento",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "local",
                    models.CharField(max_length=255, verbose_name="Local do Evento"),
                ),
                ("data", models.DateField(verbose_name="Data do Evento")),
                ("hora", models.TimeField(verbose_name="Horário do Evento")),
                (
                    "max_pessoas",
                    models.IntegerField(default=0, verbose_name="Máximo de pessoas"),
                ),
                (
                    "data_hora_limite",
                    models.DateTimeField(
                        verbose_name="Data e hora limite para inscrição"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
