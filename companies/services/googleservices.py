import asyncio
import re
import time

from companies.services.phantom_services import PhantomService
from googleapiclient.discovery import build

from companies.models import CompanyExternalData
from companies.serializers.serializer import CompanyExternalDataSerializer

api_key = "AIzaSyA2zkFGr7aL8woRLZqSQsuw9ntcEbHNvEk"
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
            resultlink = re.search(r'linkedin.com/company', result['link'])
            if resultlink:
                #CompanyExternalData.objects.create(company=company, source=result['link'], title=result['title']).save()
                agentid = PhantomService.create_phantom_agent(result['link'])
                cid = asyncio.run(PhantomService.call_phantom_agent(agentId=agentid, linkedinUrl=result['link']))
                PhantomService.fetch(containerId=cid)



    @staticmethod
    def external(company):
        query = CompanyExternalData.objects.filter(company=company)
        serializer = CompanyExternalDataSerializer(query, many=True)
        return serializer
