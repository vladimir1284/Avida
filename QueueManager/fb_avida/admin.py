from django.contrib import admin
from .models import *

admin.site.register(OrderStage)
admin.site.register(DiscardedOrder)
admin.site.register(Order)
admin.site.register(Client)
