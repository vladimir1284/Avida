# yomamabot/fb_yomamabot/urls.py
from django.conf.urls import include, url
from django.urls import path
from .views import AvidaBotView, dashboard

urlpatterns = [
                  url(r'^d0b835512d65473fa3c1064b5120bd9925880c1e30b2472ddb/?$', AvidaBotView.as_view()),
                path('', dashboard, name='dashboard'),
                  # path(r'', dashboard, 'dashboard'),
               ]