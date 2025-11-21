from django.urls import path
from .views import RestauranteListCreateView, RestauranteRetrieveUpdateDestroyView

urlpatterns = [
    path('', RestauranteListCreateView.as_view(), name='restaurante-list-create'),
    path('<int:pk>/', RestauranteRetrieveUpdateDestroyView.as_view(), name='restaurante-detail'),
]
