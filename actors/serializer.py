from rest_framework import serializers
from actors.models import Actor


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

    def validate_name(self, value):
        if Actor.objects.filter(name=value).exists():
            raise serializers.ValidationError("Ator já existe cadastrado.")
        return value
