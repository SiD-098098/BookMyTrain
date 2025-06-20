from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('train/', include('trains.urls')),
    path('bookings/', include('bookings.urls')) 
]
