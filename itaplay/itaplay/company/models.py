from __future__ import unicode_literals

from django.db import models


class Company(models.Model):
    """
    Model of company.
    """
    company_zipcode = models.CharField(max_length=20, default="")
    company_logo = models.URLField(default="")
    company_name = models.CharField(max_length=200, unique=True)
    company_mail = models.EmailField(unique=True)
    company_phone = models.CharField(max_length=50, unique=True)
    company_address = models.CharField(max_length=200)
    administrator = models.OneToOneField('authentication.AdviserUser', on_delete=models.CASCADE,blank=True, null=True)
    
    def set_company(self, arg):
        """
        Method for seting company from database.
        :param arg: dict with company fields and values.
        :return: nothing.
        """
        self = Company(**arg)
        self.save()

    def delete_company(self, company_id):
        """
        Method for deleteing company from database.
        :param company_id: primary key for searched company.
        :return: nothing.
        """
        Company.objects.get(id = company_id).delete()

    @classmethod
    def get_company(cls, company_id=None):
        """
        Classmethod for getting companies from database.
        :param company_id: primary key for searched company.
        :return: company object by id, or list of all company objects if param is 'None'.
        """
        if not company_id:
            return cls.objects.all()
        return cls.objects.get(id=company_id)
