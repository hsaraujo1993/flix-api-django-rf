from django.db.models import Count, Avg
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from movies.models import Movie
from rest_framework import generics, status, views
from movies.serializer import MovieModelSerializer, MovieListDetailSerializer
from app.permission import AppPermissionGlobal
from reviews.models import Review


# Create your views here.


class MovieListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, AppPermissionGlobal)
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieListDetailSerializer
        return MovieModelSerializer


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


class MovieStatsView(views.APIView):
    permission_classes = (IsAuthenticated, AppPermissionGlobal)
    queryset = Movie.objects.all()

    def get(self):

        total_movies = self.queryset.count()
        movies_by_genre = self.queryset.values('genre__name').annotate(count=Count('id'))
        total_reviews = Review.objects.count()
        average_stars = Review.objects.aggregate(avg_stars=Avg('stars'))['avg_stars']

        return Response({
            'total_movies': total_movies,
            'movies_by_genre': movies_by_genre,
            'total_reviews': total_reviews,
            'average_stars': round(average_stars, 1) if average_stars else 0

        }, status=status.HTTP_200_OK)







