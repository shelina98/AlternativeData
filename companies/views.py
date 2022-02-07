from rest_framework.response import Response
from companies.serializers.serializer import CompanyUploadSerializer, UserSerializer
from rest_framework import generics, status
from rest_framework import permissions
import pandas as pd
# Create your views here.
from companies.models import Company
from django.contrib.auth.models import User


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UploadFileView(generics.CreateAPIView):
    serializer_class = CompanyUploadSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        companyfile = serializer.validated_data['companyfile']
        reader = pd.read_csv(companyfile)
        for _, row in reader.iterrows():
            new_company = Company(
                name=row["name"],
                vat=row['vat'],
                country=row["country"],
                sector=row["sector"]
            )
            new_company.save()
        return Response({"status": "success"}, status.HTTP_201_CREATED)
