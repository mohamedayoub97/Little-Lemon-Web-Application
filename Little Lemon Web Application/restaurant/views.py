from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import generics

from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer, UserSerializer

# Decorators
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


# Create your views here.
def index(request):
    return render(request, 'index.html', {})

# http://127.0.0.1:8000/api/booking/
class BookingView(APIView):
#    @api_view(['GET', 'POST'])  #???
#    @permission_classes([IsAuthenticated])#???
    def get(self, request):  # GET method
        items = Booking.objects.all()
        serializer = BookingSerializer(items, many=True)
        return Response(serializer.data)  # Return JSON


# localhost:8000/restaurant/booking/tables
class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]


class MenuView(APIView):
    def post(self, request):  # POST method
        serializer = MenuSerializer(data=request.data)

        if (serializer.is_valid()):
            serializer.save()
            return Response({"status" : "success", "data" : serializer.data})  # Return JSON


class MenuItemsView(generics.ListCreateAPIView):  # Handles the POST and GET method calls.
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
#TODO:    permission_classes = [IsAuthenticated]

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):  # This class is responsible for processing GET, PUT and DELETE method calls.
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

#
# User -----------------------------------------------------------------------
#

from django.contrib.auth.models import User

class UserViewSet(ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [IsAuthenticated]

#
# Message ---------------------------------------------------------------------
#

@api_view()
@permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
def msg(request):
    return Response({"message":"This view is protected"})
