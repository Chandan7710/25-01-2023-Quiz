from rest_framework import viewsets
from rest_framework.response import Response
from home_app.models import contactform
from home_app.api.serializers import ContactformSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status

'''Class For Contact Form'''
class ContactformVS(viewsets.ViewSet):
    
    def list(self, request):
        queryset = contactform.objects.all()
        serializer = ContactformSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = contactform.objects.all()
        contact = get_object_or_404(queryset, pk=pk)
        serializer = ContactformSerializer(contact)
        return Response(serializer.data)

    def create(self, request):
        serializer = ContactformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
          
    def delete(self, request, pk):
        queryset = contactform.objects.get(pk=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

    def update(self, request, pk):
        queryset = contactform.objects.get(pk=pk)
        serializer = ContactformSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
