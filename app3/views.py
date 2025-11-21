from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Repartidor
from .serializers import RepartidorSerializer

class RepartidorListCreateView(ListCreateAPIView):
    queryset = Repartidor.objects.all()
    serializer_class = RepartidorSerializer

class RepartidorRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Repartidor.objects.all()
    serializer_class = RepartidorSerializer

# Create your views here.
