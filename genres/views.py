from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from genres.models import Genre
from rest_framework import generics, status
from genres.serializer import GenreSerializer
from app.permission import AppPermissionGlobal

# Create your views here.


class GenreListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, AppPermissionGlobal,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, AppPermissionGlobal,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    def delete(self, *args, **kwargs):
        instance = self.get_object()
        try:
            instance.delete()
            return Response({'message': 'Genre deleted successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)






