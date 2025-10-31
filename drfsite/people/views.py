from rest_framework import generics
from .models import People
from .serializer import PeopleSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict
from django.core.exceptions import ObjectDoesNotExist


class PeopleAPIView(APIView):
    def get(self, request):
        peoples = People.objects.all()
        return Response({"posts": PeopleSerializer(peoples, many=True).data})

    def post(self, request):
        serializer = PeopleSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({"errors_messages": serializer.errors})
        else:
            serializer.save()
        return Response({"post": serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)

        if not pk:
            return Response({"errors_messages": "Method PUT not allowed"})

        try:
            instance = People.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response({"Object does not exists"})

        serializer = PeopleSerializer(instance = instance, data=request.data)

        if not serializer.is_valid():
            return Response({"errors_messages": serializer.errors})
        else:
            serializer.save()

        return Response({"post": serializer.data})

    def delete(self,request,*args, **kwargs):
        pk = kwargs.get("pk",None)
        if not pk:
            return Response({"errors_messages": "Method DELETE not allowed"})

        try:
            instance = People.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response({"Object does not exists"})
        
        instance.delete()
        
        return Response({"post":f"Delete post {pk}"})