# yomamabot/fb_yomamabot/urls.py
from django.conf.urls import include, url
from django.urls import path
from .views import AvidaBotView, dashboard, get_clients, new_client, del_client, get_orders, new_order, update_order

urlpatterns = [
                url(r'^d0b835512d65473fa3c1064b5120bd9925880c1e30b2472ddb/?$', AvidaBotView.as_view()),
                path('', dashboard, name='dashboard'),
                path("get_clients/", get_clients, name='get_clients'),
                path("new_client/", new_client, name='new_client'),
                path("del_client/", del_client, name='del_client'),
                path("get_orders/", get_orders, name='get_orders'),
                path("new_order/", new_order, name='new_order'),
                path("update_order/", update_order, name='update_order'),
               ]