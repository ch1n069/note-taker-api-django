# serializes the model data 
from dataclasses import field
from .models import Note
from rest_framework import serializers



class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        # the meta describes the information in our particular class that
        model = Note
        
        fields = '__all__'