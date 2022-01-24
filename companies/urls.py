from django.urls import path
from . import views
from .views import UploadFileView
from companies.viewsets.company_viewset import CompanyViewSet
from rest_framework.routers import DefaultRouter

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

router = DefaultRouter()
router.register(r'companies', CompanyViewSet, basename='companies')
urlpatterns += router.urls
