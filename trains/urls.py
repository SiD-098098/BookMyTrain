from django.urls import path
from .views import TrainMakeView, TrainSearchView, TrainDetailView

urlpatterns = [
    path('search/', TrainSearchView.as_view(), name='train-search'),
    path('make/', TrainMakeView.as_view(), name='admin-make-train'),
    path('<int:id>/', TrainDetailView.as_view(), name='train-detail'),
]