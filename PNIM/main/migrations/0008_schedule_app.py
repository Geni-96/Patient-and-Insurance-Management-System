# Generated by Django 4.1.7 on 2023-04-05 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0007_patient_history"),
    ]

    operations = [
        migrations.CreateModel(
            name="Schedule_app",
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
                (
                    "d_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main.doctor"
                    ),
                ),
                (
                    "p_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main.patient"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Schedule Appointment",
            },
        ),
    ]
