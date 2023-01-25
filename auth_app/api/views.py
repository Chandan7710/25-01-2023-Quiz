from auth_app.api.serializers import RegistrationSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth import logout
from rest_framework import viewsets

    
# Registrtioning the new user using api and genrating the Token
class RegistrationViewSet(viewsets.ViewSet):
    
    def create(self, request):
        serializer = RegistrationSerializer(data=request.data)
         
        data = {}
        
        if serializer.is_valid():
            account = serializer.save()
        
            data['response'] = "Registration Successfyl !"
            data['username'] = account.username
            data['email'] = account.email
                
            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data, status= status.HTTP_201_CREATED)
    
# Logout the user and delete the token of the particular user
from django.contrib.auth import logout
        
class LogoutViewSet(viewsets.ViewSet):
    
    def create(self, request):
        try:
            print(request.user.auth_token)
            request.user.auth_token.delete()
        except (AttributeError):
            pass
       
        logout(request)

        return Response({"success": ("Successfully logged out.")}, status=status.HTTP_200_OK)