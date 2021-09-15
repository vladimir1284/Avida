from django.contrib import admin
from .models import OrderStage, DiscardedOrder, Order, Client

admin.site.register(OrderStage)
admin.site.register(DiscardedOrder)
admin.site.register(Order)
admin.site.register(Client)
