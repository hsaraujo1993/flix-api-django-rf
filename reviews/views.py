from django.shortcuts import render
from rest_framework.response import Response
from reviews.models import Review
from reviews.serializer import ReviewSerializer
from rest_framework import generics, status


# Create your views here.


class ReviewListCreateAPIView(generics.ListCreateAPIView):

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def delete(self, *args, **kwargs):
        instance = self.get_object()
        try:
            instance.delete()
            return Response({'message': 'Genre deleted successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


