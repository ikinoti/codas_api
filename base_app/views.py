from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q

from .models import Advocate
from .serializers import AdvocateSerializer

# Create your views here.
@api_view(['GET'])
def endpoints(request):
    data = ['/advocates', 'advocates/:username']
    return Response(data)

@api_view(['GET', 'POST'])
def advocate_list(request):
    # Handles GET request
    if request.method == 'GET':
        query = request.GET.get('query')

        if query == None:
            query = ''

        # advocate = Advocate.objects.all()
        advocate = Advocate.objects.filter(Q(username__icontains=query) | Q(bio__icontains=query))
        serializer = AdvocateSerializer(advocate, many=True)
        return Response(serializer.data)
    
    # Handles POST request
    if request.method == 'POST':
        advocate = Advocate.objects.create(username=request.data['username'], bio=request.data['bio'])
        serializer = AdvocateSerializer(advocate, many=False)

        return Response(serializer.data)
    


@api_view(['GET'])
def advocate_detail(request, username):
    advocate = Advocate.objects.get(username=username)
    serializer = AdvocateSerializer(advocate, many=False)
    return Response(serializer.data)