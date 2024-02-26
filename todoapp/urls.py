from django.urls import path
from .views import *



urlpatterns = [
    
    path('',index,name='index'),
    path('todo-detay/<slug:d_slug>/',todoDetay,name='todo-detay'),
    path('sil/',sil,name='sil'),

] 