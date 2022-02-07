from django.db.models import Count


class AggregateService:

    @staticmethod
    def numberOfcompanies(companies):
        i=0
        for com in companies:
            i += 1

        return i

    @staticmethod
    def numberOfcompaniesCountry(companies):
        return companies.values('country').annotate(number=Count('country'))

    @staticmethod
    def numberOfcompaniesSector(companies):
        return companies.values('sector').annotate(number=Count('sector'))
