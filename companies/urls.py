from django.urls import path, re_path
from . import views
from .views import UploadFileView

urlpatterns = [
    path('', views.Companies, name='companies'),

    path('api/', views.apiOverview, name='api-overview'),

    path('createcompany/', views.companyCreate, name='createcompany'),

    path('listcompany/', views.companyList, name='listcompany'),
    path('company/<str:pk>/', views.singleCompany, name='company'),

    path('updatecompany/<str:pk>/', views.companyUpdate, name='updatecompany'),
    path('deletecompany/<str:pk>/', views.companyDelete, name='deletecompany'),

    path('upload/', UploadFileView.as_view(), name='upload-file'),
]
