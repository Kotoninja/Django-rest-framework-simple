from rest_framework import generics
from .models import People, Category
from .serializer import PeopleSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets
from rest_framework.decorators import action


class PeopleViewSet(viewsets.ModelViewSet):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer

    @action(methods=["get"], detail=True)
    def category(self, request, pk=None):
        cat = Category.objects.get(pk=pk)
        return Response({"cat": cat.name})

    @action(methods=["get"], detail=False)
    def categories(self, request):
        cats = Category.objects.all()
        return Response({"cats": [c.name for c in cats]})
