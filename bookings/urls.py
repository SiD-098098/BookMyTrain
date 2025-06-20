from django.urls import path
from .views import BookingView, DeleteBookingView

urlpatterns = [
    path('book/', BookingView.as_view(), name = 'book-seat'),
    path('delete/<int:id>', DeleteBookingView.as_view(), name = 'delete-booking')
]