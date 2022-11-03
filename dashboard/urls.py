from django.urls import path
from . import views

urlpatterns = [
    path ('', views.index, name='dashboard-index'),
    path ('nacidos/', views.nacidos, name='dashboard-nacidos'),
    
    path('nacidos/delete/<int:pk>/', views.nacidos_delete,
        name='dashboard-nacidos-delete'),
    
    path ('pobrezacar/', views.pobrezacar, name='dashboard-pobrezacar'),
    
    path('pobrezacar/delete/<int:pk>/', views.pobrezacar_delete,
    name='dashboard-pobrezacar-delete'),
    
    path ('matriculacar/', views.matriculacar, name='dashboard-matriculacar'),
    
    path('matriculacar/delete/<int:pk>/', views.matriculacar_delete,
    name='dashboard-matriculacar-delete'),
]
