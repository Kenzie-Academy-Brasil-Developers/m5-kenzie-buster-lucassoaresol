from rest_framework import serializers
from .models import Movie, RatingMovie, MovieOrder


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(
        max_length=10,
        allow_null=True,
        default=None,
    )
    rating = serializers.ChoiceField(
        choices=RatingMovie.choices,
        default=RatingMovie.DEFAULT,
    )
    synopsis = serializers.CharField(allow_null=True, default=None)
    added_by = serializers.SlugRelatedField(
        read_only=True,
        slug_field="email",
        source="user",
    )

    def create(self, validated_data: dict) -> Movie:
        return Movie.objects.create(**validated_data)


class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.SlugRelatedField(
        read_only=True,
        slug_field="title",
        source="movie",
    )
    buyed_at = serializers.DateTimeField(read_only=True)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    buyed_by = serializers.SlugRelatedField(
        read_only=True,
        slug_field="email",
        source="user",
    )

    def create(self, validated_data: dict) -> MovieOrder:
        return MovieOrder.objects.create(**validated_data)
