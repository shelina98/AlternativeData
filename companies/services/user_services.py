from companies.models import Company
from companies.serializers.serializer import CompanySerializer


class UserService:

    @staticmethod
    def get_companies(user):
        query = Company.objects.filter(owner=user)
        serializer = CompanySerializer(query,many=True)
        return serializer
