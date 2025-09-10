from django.urls import path
from . import views

app_name = 'jsonpullshow'

urlpatterns = [
    path('', views.index, name='index'),
    path('api/search/', views.search_otop, name='search_otop'),
    path('api/provinces/', views.get_provinces, name='get_provinces'),
    path('api/districts/', views.get_districts, name='get_districts'),
]