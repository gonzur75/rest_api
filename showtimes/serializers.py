from movielist.models import Movie
from .models import Cinema, Screening
from rest_framework import serializers


class CinemaSerializer(serializers.ModelSerializer):
    movies = serializers.HyperlinkedRelatedField(many=True,
                                                 view_name='movie-detail',
                                                 read_only=True,
                                                 )

    class Meta:
        model = Cinema
        fields = ("name", "city", "movies")


class ScreeningSerializer(serializers.ModelSerializer):
    movie = serializers.SlugRelatedField(slug_field='title', queryset=Movie.objects.all())
    cinema = serializers.SlugRelatedField(slug_field='name', queryset=Cinema.objects.all())

    class Meta:
        model = Screening
        fields = ('cinema', 'date', 'movie')
