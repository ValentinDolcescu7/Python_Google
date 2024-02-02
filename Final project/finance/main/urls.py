from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('quote/', views.quote, name='quote'),
    path('buy/', views.buy, name='buy'),
    path('sell/', views.sell, name='sell'),
    path('history/', views.history, name='history'),
]