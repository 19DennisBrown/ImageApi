from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import dataSerializer
from .models import Data

# Create your views here.


@api_view(['GET'])
def dataView(request):
  if request.method == 'GET':
    deta = Data.objects.all()
    serialData = dataSerializer(deta, many=True)
    return Response(serialData.data)