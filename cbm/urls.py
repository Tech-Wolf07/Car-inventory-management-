from django.contrib import admin
from django.urls import path,include
from automobile.views import InventoryListCreateView, InventoryDetailView,ExpenseCreateList,ExpenseUpdateDelete,ExpensesByInventoryView
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('inventory/', InventoryListCreateView.as_view(), name='inventory_list_create'),
    path('inventory/<int:pk>', InventoryDetailView.as_view(), name='inventory_detail'),
    
    path('expense/', ExpenseCreateList.as_view(), name='expense_create_list'),
    path('expense/<int:pk>', ExpenseUpdateDelete.as_view(), name='expense_detail'),
    path('expenses/inventory/<int:inventory_id>/', ExpensesByInventoryView.as_view(), name='expenses-by-inventory'),

]