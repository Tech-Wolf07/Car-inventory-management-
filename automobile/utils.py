# from django.db import transaction, connection
# from .models import Inventory

# def reorder_ids():
#     """
#     Reassign sequential IDs to all inventory items after deletion.
#     This will ensure there are no gaps in IDs.
#     """
#     with transaction.atomic():
#         # Fetch all items ordered by their current ID
#         items = Inventory.objects.order_by('id')

#         # Start updating IDs from 1 and increment sequentially
#         for idx, item in enumerate(items, start=1):
#             if item.id != idx:
#                 item.id = idx  # Reassign the ID to be in sequence
#                 item.save(update_fields=['id'])  # Save the updated ID

#         # Reset the sequence to the last id value
#         with connection.cursor() as cursor:
#             cursor.execute("""
#                 SELECT setval(pg_get_serial_sequence('inventory_inventory', 'id'), 
#                               (SELECT max(id) FROM 'inventory_inventory'))
#             """)

