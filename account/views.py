from rest_framework.views import APIView
from rest_framework.response import Response
from .serilizers import RegisterSerializer
from django.contrib.auth import authenticate 
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'message': 'User registered successfully'}, status=201)
        return Response(serializer.errors, status=400)


# Login view to authenticate user and return token

class LoginAPI(APIView):

    def post(self, request):
        username=request.data.get('username')
        password=request.data.get('password')

        user = authenticate(username=username, password=password)
        if user:
            token,_ = Token.objects.get_or_create(user=user) #This is a Python trick. get_or_create returns two things (the token and a True/False flag). We only care about the token, so we "throw away" the second part into the underscore.
            return Response({'token': token.key}, status=200)
        return Response({'error': 'Invalid credentials'}, status=400)

class ProfileAPI(APIView):
    
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            'username': user.username,
            'email': user.email
        }, status=200)