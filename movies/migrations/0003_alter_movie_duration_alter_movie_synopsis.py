# Generated by Django 4.1.7 on 2023-02-23 05:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("movies", "0002_movieorder_movie_orders"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="duration",
            field=models.CharField(default=None, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="movie",
            name="synopsis",
            field=models.TextField(default=None, null=True),
        ),
    ]
