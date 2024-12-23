from rest_framework import serializers

from actors.serializer import ActorSerializer
from genres.models import Genre
from genres.serializer import GenreSerializer
from movies.models import Movie
from django.db.models import Avg


class MovieModelSerializer(serializers.ModelSerializer):


    class Meta:
        model = Movie
        fields = '__all__'


    def validate_release_date(selfs, value):
        if value.year < 1900:
            raise serializers.ValidationError('A data de lançamento não pode ser anterior a 1990.')
        return value

    def validate_title(self, value):
        if Movie.objects.filter(title=value).exists():
            raise serializers.ValidationError("Titulo já existe cadastrado.")
        return value


class MovieListDetailSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)
    genre = GenreSerializer()
    # Adicionando campo rate no model: Campo SerializerMethodField é um campo calculado
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'actors', 'release_date', 'rate', 'resume']

    # Função responsável pelo cálculo da média das avaliações no campo rate
    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']
        if rate:
            return round(rate, 1)
        return None
