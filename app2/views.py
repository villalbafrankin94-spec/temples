from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Restaurante
from .serializers import RestauranteSerializer

class RestauranteListCreateView(ListCreateAPIView):
    queryset = Restaurante.objects.all()
    serializer_class = RestauranteSerializer

class RestauranteRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Restaurante.objects.all()
    serializer_class = RestauranteSerializer

# Create your views here.
