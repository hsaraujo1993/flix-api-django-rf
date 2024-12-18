from django.core.serializers import serialize
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import serializers
from movies.models import Movie
from rest_framework import generics, status
from movies.serializer import MovieModelSerializer
from app.permission import AppPermissionGlobal


# Create your views here.


class MovieListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, AppPermissionGlobal)
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer


class MovieRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, AppPermissionGlobal)
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        try:
            instance.delete()
            return Response({'message': 'Movie deleted successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




