from django.urls import path
from .views import FlowerPostListCreateView
from .views import FlowerPostRetrieveUpdateDestroyView

urlpatterns = [
    path('', FlowerPostListCreateView.as_view()),
    path('<int:id>/', FlowerPostRetrieveUpdateDestroyView.as_view())
]