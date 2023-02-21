from django.db import models


class RatingMovie(models.TextChoices):
    PG = "PG"
    PG_13 = "PG-13"
    R = "R"
    NC_17 = "NC-17"
    DEFAULT = "G"


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, null=True)
    rating = models.CharField(
        max_length=20,
        choices=RatingMovie.choices,
        default=RatingMovie.DEFAULT,
    )
    synopsis = models.TextField(null=True)

    user = models.ForeignKey(
        "accounts.User", on_delete=models.CASCADE, related_name="movies"
    )
