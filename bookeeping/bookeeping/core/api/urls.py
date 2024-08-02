from django.urls import path
from rest_framework.routers import DefaultRouter

from bookeeping.core.api.views import BusinessViewSet, ItemsViewSet, InventoryViewSet, InvoicesViewSet, PartiesViewSet, TransactionsViewSet

urlpatterns = []


#Business urls
business_router = DefaultRouter()
business_router.register(r"business", BusinessViewSet, basename="business")
urlpatterns += business_router.urls

#Items urls
items_router = DefaultRouter()
items_router.register(r"items", ItemsViewSet, basename="items")
urlpatterns += items_router.urls

#Inventory urls
inventory_router = DefaultRouter()
inventory_router.register(r"inventory", InventoryViewSet, basename="inventory")
urlpatterns += inventory_router.urls

#Invoices urls
invoices_router = DefaultRouter()
invoices_router.register(r"invoices", InvoicesViewSet, basename="invoices")
urlpatterns += invoices_router.urls

#Parties urls
parties_router = DefaultRouter()
parties_router.register(r"parties", PartiesViewSet, basename="parties")
urlpatterns += parties_router.urls

#Transactions urls
transactions_router = DefaultRouter()
transactions_router.register(r"transactions", TransactionsViewSet, basename="transactions")
urlpatterns += transactions_router.urls