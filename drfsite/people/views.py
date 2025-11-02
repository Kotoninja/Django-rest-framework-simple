from rest_framework import generics
from .models import People
from .serializer import PeopleSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets

class PeopleViewSet(viewsets.ModelViewSet):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer