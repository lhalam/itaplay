from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.forms.models import model_to_dict


class Company(models.Model):
    """
    Model of company.
    """
    zipcode = models.CharField(max_length=20, default="")
    logo = models.URLField(default="")
    name = models.CharField(max_length=200, unique=True)
    mail = models.EmailField(unique=True)
    phone = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=200)
    administrator = models.OneToOneField('authentication.AdviserUser', on_delete=models.SET_NULL, blank = True, null = True)
    
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

    def get_users(self):
        """
        Method for getting users of company from database.
        :return: list with users dictionaries.
        """  
        users = [user for user in User.objects.all() if hasattr(user, 'adviseruser')]
        company_users = [model_to_dict(user.adviseruser) for user in users if user.adviseruser.id_company==self]
        for user_ in company_users:           
            [user_.update({'first_name' : user.first_name, 
                          'last_name' : user.last_name, 
                          'username' : user.username, 
                          'email' : user.email,}) for user in users if user.adviseruser.id==user_["id"]]
        return company_users

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
