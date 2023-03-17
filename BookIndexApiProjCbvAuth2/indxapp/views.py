from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from .models import Phrase
from .serializers import PhraseSerializers
from rest_framework import viewsets
from rest_framework.decorators import action
from .pagination import MyPageNumberPagination
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from django.contrib.auth.models import User

def home(request):
    return HttpResponse(
        '<center><h1 style="background-color:powderblue;">Welcome to Phrase Api</h1></center>'
    )

#!Model viewsets
class PhraseMVS(viewsets.ModelViewSet):
    permission_classes=(IsAuthenticated,)
    queryset=Phrase.objects.all()
    serializer_class=PhraseSerializers
    pagination_class=MyPageNumberPagination
    filterset_fields=['text_number','phrase_number','phrase_content']

    
class UserOperations(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PhraseSerializers
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated ]
    # permission_classes = [IsAuthenticated]
    #permission_classes = [IsAddedByUserOrReadOnly]

    @action(methods=["GET"], detail=False) #> browser adresinde "phreas_count" ile çağır.
    def phrase_count(self, request):
        phrase_count=Phrase.objects.count()
        count={
            "Mount Of Phrases":phrase_count
        }
        return Response(count)      
   
