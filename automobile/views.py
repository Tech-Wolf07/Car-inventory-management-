from .models import Inventory, Expenses
from .serializers import InventorySerializer, ExpensesSerializer, RegisterSerializer,LoginSerializer
from rest_framework import generics,status
from rest_framework.response import Response
from django.db.models import Sum, Q
from django.db import  connection
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView 
from rest_framework.authentication import TokenAuthentication, authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from django.core.paginator import Paginator

# Generic Views
# List and Create Inventory items
class InventoryListCreateView(generics.ListCreateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    
    def get_queryset(self):
         queryset = super().get_queryset()
         queryset = queryset.annotate(calculated_total_expenses = Sum('expenses__amount', filter=~Q(expenses__amount=0)))
         return queryset
    
# Update and Delete Inventory items
class InventoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    
    def destroy(self, request, *args, **kwargs):
            instance = self.get_object()
            instance.delete() 
            
            try:
                with connection.cursor() as cursor:
                    # Reassign IDs (this part was correct)
                    cursor.execute("""
                        WITH CTE AS (
                            SELECT id, ROW_NUMBER() OVER (ORDER BY id) AS new_id
                            FROM automobile_inventory
                        )
                        UPDATE automobile_inventory
                        SET id = CTE.new_id
                        FROM CTE
                        WHERE automobile_inventory.id = CTE.id;
                    """)

                    # Reset the sequence (this is critical)
                    cursor.execute("""
                        DO $$
                        DECLARE
                            max_id INT;
                        BEGIN
                            -- Get the maximum ID from the table
                            SELECT MAX(id) INTO max_id FROM automobile_inventory;

                            -- If there are no records, start the sequence at 1
                            IF max_id IS NULL THEN
                                max_id := 1;
                            END IF;

                            -- Reset the sequence for 'id' based on max_id
                            PERFORM setval(pg_get_serial_sequence('automobile_inventory', 'id'), max_id, false);
                        END $$;
                    """)

                # Return the success response
                return Response({"message": "Inventory item deleted. "}, status=status.HTTP_200_OK)

            except Exception as e:
                return Response({"error": f"Failed to reset IDs: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# ----------------------------------------------------------------------------------

class ExpenseCreateList(generics.ListCreateAPIView):
    queryset = Expenses.objects.all()
    serializer_class = ExpensesSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    
# Retrieve, Update, and Delete a single expense 
class ExpenseUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expenses.objects.all()
    serializer_class = ExpensesSerializer 
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    
    def destroy(self, request, *args, **kwargs):
            instance = self.get_object()
            instance.delete()

            try:
                with connection.cursor() as cursor:
                    # Reassign IDs (this part was correct)
                    cursor.execute("""
                        WITH CTE AS (
                            SELECT id, ROW_NUMBER() OVER (ORDER BY id) AS new_id
                            FROM automobile_expenses
                        )
                        UPDATE automobile_expenses
                        SET id = CTE.new_id
                        FROM CTE
                        WHERE automobile_expenses.id = CTE.id;
                    """)

                    # Reset the sequence (this is critical)
                    cursor.execute("""
                        DO $$
                        DECLARE
                            max_id INT;
                        BEGIN
                            -- Get the maximum ID from the table
                            SELECT MAX(id) INTO max_id FROM automobile_expenses;

                            -- If there are no records, start the sequence at 1
                            IF max_id IS NULL THEN
                                max_id := 1;
                            END IF;

                            -- Reset the sequence for 'id' based on max_id
                            PERFORM setval(pg_get_serial_sequence('automobile_expenses', 'id'), max_id, false);
                        END $$;
                    """)

                # Return the success response
                return Response({"message": "Expense deleted. "}, status=status.HTTP_200_OK)

            except Exception as e:
                return Response({"error": f"Failed to reset IDs: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)        

# Delete expense with inventory_id
class ExpensesByInventoryView(ListAPIView):
        queryset = Expenses.objects.all()
        serializer_class = ExpensesSerializer
        permission_classes = [IsAuthenticated]
        authentication_classes = [TokenAuthentication]

        def get_queryset(self):
            inventory_id = self.kwargs.get('inventory_id')  # Extract inventory_id from the URL
            return Expenses.objects.filter(inventory_id=inventory_id)
        
        
class RegisterView(APIView):
    permission_classes =[AllowAny]
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data = data)
        if not serializer.is_valid():
            return Response({'message':serializer.errors}, status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response({'message':'User created.'}, status.HTTP_201_CREATED)
    

class LoginView(APIView):
    permission_classes =[AllowAny]
    def post(self, request):
        data = request.data
        serializer = LoginSerializer(data = data)
        if not serializer.is_valid():
            return Response({'message':serializer.errors}, status.HTTP_400_BAD_REQUEST)
        
        user  = authenticate(username = serializer.validated_data['username'],password = serializer.validated_data['password'] )
        if not user:
            return Response({'error':'User not found'}, status.HTTP_401_UNAUTHORIZED)

        token, _ = Token.objects.get_or_create(user = user)
        return Response( {'token' : str(token)}, status.HTTP_201_CREATED)
