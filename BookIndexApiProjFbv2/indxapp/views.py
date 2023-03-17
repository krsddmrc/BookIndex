from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
import rest_framework
from rest_framework import serializers


from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Phrase
from .serializers import PhraseSerializers

from rest_framework import status

def home(request):
    return HttpResponse(
        '<center><h1 style="background-color:powderblue;">Welcome to Phrase Api</h1></center>'
    )

@api_view()
def hello_world(request):
    return Response({"message": "Hello, world!"})

@api_view(['GET'])
def phraseList(request):
    querset =  Phrase.objects.all()    
    serializer = PhraseSerializers(querset, many=True)
   
    return Response(serializer.data)


@api_view(['POST'])
def phraseCreate(request):

    serializer = PhraseSerializers(data = request.data)
    
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def phraseListCreate(request):
    if request.method == "GET":
        querset =  Phrase.objects.all()    
        serializer = PhraseSerializers(querset, many=True)
    
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = PhraseSerializers(data = request.data)
    
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['GET','PUT', 'DELETE'])
def phraseUpdate(request, pk):
    
    querset =  Phrase.objects.get(id = pk)
    
    if request.method == "GET":
        serializer = PhraseSerializers(querset)
    
        return Response(serializer.data)
        
    elif request.method == "PUT":
        
        serializer = PhraseSerializers(instance=querset,  data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == "DELETE":
      
        querset.delete()
        return Response("Item Deleted")
        
    

@api_view(['DELETE'])
def phraseDelete(request, pk):
    
    querset =  Phrase.objects.get(id = pk)
    querset.delete()
    return Response("Item Deleted")