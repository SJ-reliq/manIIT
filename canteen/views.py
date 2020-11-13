from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from canteen.models import canteen_model
from canteen.serializers import CanteenSerializer
import random
import math
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi 
from twilio.rest import Client
from django.conf import settings 
from canteen.models import canteen_model
user_response = openapi.Response('Response', CanteenSerializer)
TWILIO_ACCOUNT_SID = "AC9955aeb26c18f100c937d33b81aff64d"
TWILIO_AUTH_TOKEN ="d2decd6b35a37989a68f07eab16c444d"
TWILIO_NUMBER = "+12056229627"

@swagger_auto_schema(method='post', request_body=CanteenSerializer)
@api_view(['POST'])
def signup(request, format=None):
      if request.method == 'POST':
        serializer = CanteenSerializer(data=request.data)
        if serializer.is_valid():
            digits = [i for i in range(0, 10)]
            random_str = ""

            for i in range(6):
                index = math.floor(random.random() * 10)
                random_str += str(digits[index])
            
            try:
                client = Client(TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN)
                client.messages.create(to=request.data['phone'],
                                   from_=TWILIO_NUMBER,
                                   body=random_str)
            except:
                return Response(client.errors, status=status.HTTP_400_BAD_REQUEST)

            serializer.save()
            newdict={'otp':random_str}
            newdict.update(serializer.data)
            return Response(newdict, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



user_response = openapi.Response('Response', CanteenSerializer)
@swagger_auto_schema(method='post', request_body=CanteenSerializer,responses={200: user_response})
@api_view(['POST'])
def login(request, format=None):
    """
    List all code items, or create a new item.
    """

    try:
        user1= canteen_model.objects.get(phone=request.data['phone'],password=request.data['password'],activation=True)
    except canteen_model.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    serializer = CanteenSerializer(user1)
    return Response(serializer.data)


@swagger_auto_schema(method='get',responses={200: user_response})
@swagger_auto_schema(method='post', request_body=CanteenSerializer,responses={200: user_response})
@api_view(['GET', 'POST'])
def canteen_list(request, format=None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        canteens = canteen_model.objects.all()
        serializer = CanteenSerializer(canteens, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CanteenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@swagger_auto_schema(method='get',responses={200: user_response})
# 'methods' can be used to apply the same modification to multiple methods
@swagger_auto_schema(method='delete',request_body=None,)
@swagger_auto_schema(method='put', request_body=CanteenSerializer)      
@api_view(['GET', 'PUT', 'DELETE'])
def canteen_detail(request, canteen_id, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        canteen = canteen_model.objects.get(canteen_id=canteen_id)
    except canteen_model.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CanteenSerializer(canteen)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CanteenSerializer(canteen, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        canteen.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    