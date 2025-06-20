from .models import Train
from .serializers import TrainListSerializer, TrainSearchSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class TrainSearchView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        trains = Train.objects.all()
        train_list = TrainListSerializer(trains, many = True)
        return Response(train_list.data)
        
@method_decorator(csrf_exempt, name='dispatch')    
class TrainDetailView(APIView):
    authentication_classes = [TokenAuthentication]

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        elif self.request.method == 'DELETE':
            return [IsAdminUser()]
        elif self.request.method == 'PUT':
            return [IsAdminUser()]
        return [IsAdminUser()]

    def get(self, request, id):
        try:
            train = Train.objects.get(id=id)
        except Train.DoesNotExist:
            return Response({"error": "Train not found"})

        serializer = TrainListSerializer(train)
        return Response(serializer.data)
    
    def delete(self,request, id):
        deleted_count, _ = Train.objects.filter(id=id).delete()
        if deleted_count == 0:
            return Response({"ERROR": "Train not found"})
        return Response({"Message" : "Train deleted successfully"})
    
    def put(self, request, id):
        try:
            train = Train.objects.get(id=id)
        except Train.DoesNotExist:
            return Response({"error": "Train not found"})
        
        serializer = TrainListSerializer(train, data = request.data, partial = True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
@method_decorator(csrf_exempt, name='dispatch')
class TrainMakeView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        serializer = TrainListSerializer(data = request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    

