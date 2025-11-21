from django.urls import path
from .views import RepartidorListCreateView, RepartidorRetrieveUpdateDestroyView

urlpatterns = [
    path('', RepartidorListCreateView.as_view(), name='repartidor-list-create'),
    path('<int:pk>/', RepartidorRetrieveUpdateDestroyView.as_view(), name='repartidor-detail'),
]
