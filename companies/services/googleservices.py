from googleapiclient.discovery import build

from companies.models import CompanyExternalData
from companies.serializers.serializer import CompanyExternalDataSerializer

api_key = "AIzaSyBl8DTGupdA73zdLDs9hZbbCJk2Or28P6Y"
cse_id = "ea9823706ac6eff0f"


class GoogleService:

    @staticmethod
    def google_search(search_term, **kwargs):
        service = build("customsearch", "v1", developerKey=api_key)
        res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
        return res['items']

    @staticmethod
    def process_results(results, company):
        for result in results:
            CompanyExternalData.objects.create(company=company,
                                               source=result['link'],
                                               title=result['title']).save()

    @staticmethod
    def external(company):
        query = CompanyExternalData.objects.filter(company=company)
        serializer = CompanyExternalDataSerializer(query, many=True)
        return serializer
