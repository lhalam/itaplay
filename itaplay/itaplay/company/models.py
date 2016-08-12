from __future__ import unicode_literals

from django.db import models


class Company(models.Model):
    """account for company"""
    company_zipcode = models.CharField(max_length=20, default="")
    company_logo = models.URLField(default="")
    company_name = models.CharField(max_length=200, unique=True)
    company_mail = models.EmailField(unique=True)
    company_phone = models.CharField(max_length=50, unique=True)
    company_address = models.CharField(max_length=200)
    administrator = models.IntegerField(default=1) # will be foreign key
    
    def set_company(self, arg):
        self = Company(**arg)
        self.save()

    def delete_company(self, company_id):
        self = Company.objects.get(id = company_id)
        self.delete()

    @classmethod
    def get_company(cls, company_id=None):
        """
        returns company instance by id or all instances
        """
        if company_id==None:
            return cls.objects.all()
        return cls.objects.get(id=company_id)

        