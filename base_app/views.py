from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET', 'POST'])
def endpoints(request):
    data = ['/advocates', 'advocates/:username']
    return Response(data)

@api_view(['GET'])
def advocate_list(request):
    data = ['Kinoti', 'Cynthia', 'Kinya']
    return Response(data)

@api_view(['GET'])
def advocate_detail(request, username):
    data = username
    return Response(data)