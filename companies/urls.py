from django.urls import path
from . import views

urlpatterns = [
    path('', views.Companies, name='companies'),
    path('company/<str:pk>/', views.singleCompany, name='company'),

    path('api/', views.apiOverview, name='api-overview'),

    path('createcompany/', views.companyCreate, name='createcompany'),
    path('listcompany/', views.companyList, name='listcompany'),
    path('updatecompany/<str:pk>/', views.companyUpdate, name='updatecompany'),

]
