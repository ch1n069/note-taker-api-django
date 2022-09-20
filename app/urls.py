from django.contrib import admin
from django.urls import path , include
from app.views import NotesViewset 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('/posts',NotesViewset)

urlpatterns = [
    path('', include(router.urls)),
]
