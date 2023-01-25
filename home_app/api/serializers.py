from rest_framework import serializers
from home_app.models import contactform

class ContactformSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = contactform
        fields = "__all__"
