from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('wines/', views.wines, name='wines'),
    path('red-wines/', views.wines_page_red, name='red-wines'),
    path('white-wines/', views.wines_page_white, name='white-wines'),
    path('sparkling-wines/', views.wines_page_sparkling, name='sparkling-wines'),
    path('test/', views.wines_all, name='test'),
    path('db/', views.db, name='db')
    ]
