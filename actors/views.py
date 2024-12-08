from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response

from actors.models import Actor
from actors.serializer import ActorSerializer

# Create your views here.


class ActorListCreateAPIView(generics.ListCreateAPIView):

    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def delete(self, *args, **kwargs):
        instance = self.get_object()
        try:
            instance.delete()
            return Response({'message': 'Actor deleted successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

