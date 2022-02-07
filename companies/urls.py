from django.urls import path
from companies.views import UploadFileView, UserList, UserDetail
from companies.viewsets.company_viewset import CompanyViewSet
from rest_framework.routers import DefaultRouter
from companies.viewsets.CompanyExternalData_viewset import CompanyExternalDataViewSet
from companies.viewsets.user_viewset import UserViewSet

urlpatterns = [
    path('UploadWithCSV/', UploadFileView.as_view(), name='upload-file'),
    path('users/', UserList.as_view()),
    path('user/<int:pk>/', UserDetail.as_view()),
]

router = DefaultRouter()
router.register(r'companies', CompanyViewSet, basename='companies')
router.register(r'usersWITHVS', UserViewSet, basename='usersWITHVS')
router.register(r'companies_external_data', CompanyExternalDataViewSet, basename='companies_external_data')
urlpatterns += router.urls
