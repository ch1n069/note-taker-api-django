from django.shortcuts import render
from app.models import Note
from rest_framework import viewsets
from app.serializers import NoteSerializer
# Create your views here.
# the view sets allow us to create the http responses


class NotesViewset(viewsets.ModelViewSet):
    '''this is responsible for fetching all the notes '''
    serializer_class =  NoteSerializer
    queryset = Note.objects.all()