# serializes the model data 
from dataclasses import field
from .models import Note
from rest_framework import 



class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        # the meta describes the information in our particular class that
        model = Note
        
        field = '__all__'