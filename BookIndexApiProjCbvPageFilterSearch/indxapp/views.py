from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
import rest_framework
from rest_framework.response import Response
from .models import Phrase
from rest_framework import serializers
from .serializers import PhraseSerializers
from rest_framework import status

from rest_framework.views import APIView 
from rest_framework import mixins       
from rest_framework.generics import GenericAPIView  
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView  
from rest_framework import viewsets
from rest_framework.decorators import action
from .pagination import MyPageNumberPagination

def home(request):
    return HttpResponse(
        '<center><h1 style="background-color:powderblue;">Welcome to Phrase Api</h1></center>'
    )

#! class_based views
#class PhraseList(APIView): 
#    def get(self, request):
#        phrases = Phrase.objects.all()
#        serializer = PhraseSerializers(phrases, many=True)
#        return Response(serializer.data)
#
#    def post(self, request):
#        serializer = PhraseSerializers(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#        return Response(serializer.data)    
#
#class PhraseDetail(APIView):
#
#    def get_obj(self, pk):
#        return get_object_or_404(Phrase, pk=pk)
#
#    def get(self, request, pk):
#        phrase = self.get_obj(pk)
#        serializer = PhraseSerializers(phrase)
#        return Response(serializer.data)
#
#    def put(self, request, pk):
#        phrase = self.get_obj(pk)
#        serializer = PhraseSerializers(instance=phrase, data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#    def delete(self, request, pk):
#        todo = self.get_obj(pk)
#        todo.delete()
#        data = {
#            "message": "Phrase succesfully deleted."
#        }
#        return Response(data, status=status.HTTP_204_NO_CONTENT)

#! GENERİC API Views  
# Attributes : queryset, serializer_class, lookup_field, lookup_url_kwarg
# Methods : get_queryset(self), get_object(self) : 

#class PhraseList(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
#    queryset=Phrase.objects.all()
#    serializer_class=PhraseSerializers
#
#    def get(self, request, *args, **kwargs):  
#        return self.list(request, *args, **kwargs)
#    
#    def post(self, request, *args, **kwargs):  
#            return self.create(request, *args, **kwargs)

#!CONCRETE VİEW CLASSES 
#class PhraseListCreate(ListCreateAPIView):
#    queryset=Phrase.objects.all()
#    serializer_class=PhraseSerializers
#
#class PhraseGetUpdateDelete(RetrieveUpdateDestroyAPIView): 
#    queryset=Phrase.objects.all()
#    serializer_class=PhraseSerializers
#    lookup_field='id'  

#!Model viewsets
class PhraseMVS(viewsets.ModelViewSet):
    queryset=Phrase.objects.all()
    serializer_class=PhraseSerializers
    pagination_class=MyPageNumberPagination
    filterset_fields=['text_number','phrase_number','phrase_content']

    @action(methods=["GET"], detail=False) #> browser adresinde "phreas_count" ile çağır.
    def phrase_count(self, request):
        phrase_count=Phrase.objects.count()
        count={
            "Mount Of Phrases":phrase_count
        }
        return Response(count)      
   
