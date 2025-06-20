from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, LoginSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            user_obj = User.objects.create_user(
                username = serializer.validated_data['username'],
                password = serializer.validated_data['password']
            )
            token, created = Token.objects.get_or_create(user = user_obj)
            return Response({
                    "status" : True,
                    "data" : {'token' : token.key }
            })
        return Response(serializer.errors)
    
class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data = request.data)
        if serializer.is_valid():
            username = serializer.data['username']
            password = serializer.data['password']
            user_obj =  authenticate(username = username, password = password)
            if user_obj:
                token, created = Token.objects.get_or_create(user = user_obj)
                return Response({
                    "status" : True,
                    "data" : {'token' : token.key}
                })
            return Response({
               "status" : False,
               "data" : serializer.errors
            })