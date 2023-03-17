from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Phrase
from .serializers import PhraseSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
def home(request):
 return HttpResponse('<h1>API Page</h1>')

@api_view(['GET', 'POST'])
def phrase_api(request):
    if request.method == 'GET':
        phrases = Phrase.objects.all()
        serializer = PhraseSerializer(phrases, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PhraseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Phrase {serializer.validated_data.get('phrase_number')}saved successfully!"}
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def phrase_api_get_update_delete(request, pk):
    phrase = get_object_or_404(Phrase, pk=pk)
    if request.method == 'GET':
        serializer = PhraseSerializer(phrase)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = PhraseSerializer(phrase, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Phrase {phrase.phrase_number} updated successfully"
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = PhraseSerializer(phrase, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Phrase {phrase.phrase_number} updated successfully"
            }
            return Response(data)
    elif request.method == 'DELETE':
        phrase.delete()
        data = {
            "message": f"Phrase {phrase.phrase_number} deleted successfully"
        }
        return Response(data)   