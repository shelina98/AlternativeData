import uuid

from django.db import models


# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=200,  null=False, blank=False)
    vat = models.CharField(max_length=200, unique=True, editable=False, null=False, blank=False)
    country = models.CharField(max_length=200, blank=True, null=True)
    sector = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)


