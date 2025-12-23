from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from .models import Cows,Barns
from .serializers import CowsSerializer,BarnsSerializer


@api_view(["GET"])
@permission_classes([AllowAny])
def get_cows_example(req):
    """
    Example of a Function-Based View (FBV) accessing SQL Server data.
    """
    # 1. Fetching data from the database using Django ORM
    # This works identically for SQL Server once configured in settings.py
    cows = Cows.objects.all()
    
    # 2. Serializing the data
    serializer = CowsSerializer(cows, many=True)
    
    # 3. Returning the response
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_barns_example(req):
    barns = Barns.objects.all()
    serializer = BarnsSerializer(barns,many=true)
    return Response(serializer.data)