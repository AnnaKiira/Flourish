from django.urls import path
from .views import CommentCreateView, CommentDestroyView

urlpatterns = [
    path('', CommentCreateView.as_view()),
    path('<int:pk>/', CommentDestroyView.as_view())
]