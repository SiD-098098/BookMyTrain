from .models import Booking
from .serializers import BookingSerializer, BookingResponseSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class BookingView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = BookingSerializer(data=request.data)
        
        if serializer.is_valid():
            train_id = serializer.validated_data['train'].id

            train = serializer.validated_data['train']
            if train.booked_seats >= train.total_seats:
                return Response({"error": "Train is fully booked."})
            
            booked_seats = set(
                Booking.objects.filter(train_id = train_id).values_list('seat_number', flat = True)
            )

            for seat_num in range(1, train.total_seats + 1):
                if seat_num not in booked_seats:
                    available_seat = seat_num
                    break
            else:
                return Response({"error" : "No valid seat found"})

            booking = serializer.save(user=request.user, seat_number = available_seat)
            train.booked_seats += 1
            train.save()

            return Response(BookingSerializer(booking).data)

        return Response(serializer.errors)
    
    def get(self, request):
        bookings = Booking.objects.filter(user = request.user)
        serializer = BookingResponseSerializer(bookings, many = True)
        return Response(serializer.data)
    

class DeleteBookingView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, id):
        user = request.user
        try:
            booking = Booking.objects.select_related('train').get(id=id, user=user)
        except Booking.DoesNotExist:
            return Response({"error": "Booking not found"})

        train = booking.train  

        train.booked_seats -= 1
        train.save()

        booking.delete()

        return Response({"message": "Booking deleted successfully"})

