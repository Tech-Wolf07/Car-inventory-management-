from django.shortcuts import render,get_object_or_404
from .models import Inventory,Expensens
from django.http import HttpResponse, request, JsonResponse
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from .serializers import InventorySerializer, ExpensesSerializer
from rest_framework import generics


# ====================================================
# cars views

@api_view(['POST'])
def addCar(request):
    serializer = InventorySerializer(data = request.data)
    
    if serializer.is_valid() == False:
        return Response(serializer.errors)

    serializer.save()
    return Response("Successfully Added a Car!")
    
    
@api_view(['GET'])
def getCars(resquest):
    data = list(Inventory.objects.values())
    return JsonResponse(data,safe=False)


@api_view(['PUT'])
def updateCar(resquest):
    data = list(Inventory.objects.values())
    return JsonResponse(data,safe=False)


@api_view(['DELETE'])
def deleteCar(resquest):
    data = list(Inventory.objects.values())
    return JsonResponse(data,safe=False)

# ====================================================
# expense views

@api_view(['POST'])
def addExpense(request):
    serializer = InventorySerializer(data=request.data)
    if serializer.is_valid():
         serializer.save()
         return Response(serializer.data)
    else:
        return Response(serializer.errors)
    

@api_view(['GET'])
def getExpenses(request):
   expenses = Expensens.objects.all()
   serializer = ExpensesSerializer(expenses, many=True)
   return Response(serializer.data)

@api_view(['PUT'])
def updateExpense(resquest):
    data = list(Inventory.objects.values())
    return JsonResponse(data,safe=False)


@api_view(['DELETE'])
def deleteExpense(resquest):
    data = list(Inventory.objects.values())
    return JsonResponse(data,safe=False)