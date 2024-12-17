from rest_framework import serializers
from genres.models import Genre


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'


    def validate_name(self, value):
        if Genre.objects.filter(name=value).exists():
            raise serializers.ValidationError("O gênero já está cadastrado.")
        return value
