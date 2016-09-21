import json

from django.test import Client
from django.test import TestCase
from django.contrib.auth.models import User

from company.models import Company
from company.views import CompanyListView, CompanyDetailsView
from authentication.models import AdviserUser

from django.core.urlresolvers import reverse


class CompanyViewTestCase(TestCase):

    def setUp(self):
        
        User.objects.create(
            username="test@superadmin.com",
            is_superuser=True,
            email="super@test.com",
            id=1
        )

        User.objects.create(
            username="test@test.com",
            is_superuser=False,
            email="test@test.com",
            id=2
        )

        User.objects.create(
            username="test3@test.com",
            is_superuser=False,
            email="test3@test.com",
            id=3
        )

        User.objects.create(
            username="test4@test.com",
            is_superuser=False,
            email="test4@test.com",
            id=4
        )

        user = User.objects.get(id=1)
        user.set_password("password")
        user.save()

        user = User.objects.get(id=2)
        user.set_password("password")
        user.save()

        user = User.objects.get(id=3)
        user.set_password("password")
        user.save()

        user = User.objects.get(id=4)
        user.set_password("password")
        user.save()
        
        Company.objects.create(
            id=1,
            company_zipcode="79008",
            company_logo="http://test.test",
            company_name="testcompany",
            company_mail="test@test.test",
            company_address= "testaddress",
            company_phone="+380901234567",      
        )

        Company.objects.create(
            id=2,
            company_zipcode="794508",
            company_logo="http://test2.test",
            company_name="testcompany2",
            company_mail="test2@test.test",
            company_address= "testaddress2",
            company_phone="+380901234677",
        )

        AdviserUser.objects.create(
            user=User.objects.get(id=2),
            id_company=Company.objects.get(id=1),
            id=1
        )
        
        AdviserUser.objects.create(
            user=User.objects.get(id=3),
            id_company=Company.objects.get(id=1),
            id=2
        )    
        
        AdviserUser.objects.create(
            user=User.objects.get(id=4),
            id_company=Company.objects.get(id=2),
            id=3
        )    


        

        self.client = Client()
        self.client.login(username="test@superadmin.com", password="password")

    def test_get_list(self):
        url = reverse('company_list_view')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
       
        self.client = Client()
        self.client.login(username="test@test.com", password="password")
        response = self.client.get(url)
        company = json.loads(response._container[0])[0]
        self.assertEqual(company.get("id"), 1)
        self.assertEqual(response.status_code, 200)
    

    def test_get_object(self):
        url = reverse('company_details_view', args=[1])
        response = self.client.get(url)
        company = json.loads(response._container[0])["company"]
        self.assertEqual(company.get("id"), 1)
        self.assertEqual(response.status_code, 200)
        
        self.client = Client()
        self.client.login(username="test@test.com", password="password")
        response = self.client.get(url)
        company = json.loads(response._container[0])["company"]
        self.assertEqual(company.get("id"), 1)
        self.assertEqual(response.status_code, 200)

        url = reverse('company_details_view', args=[2])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 400)

        

    def test_post(self):
        data = json.dumps({
                   "id" : 3,
                    "company_zipcode" : "12344441",
                    "company_logo" : "http://test.tst",
                    "company_name" : "testcompany3",
                    "company_mail" : "test@test.com",
                    "company_address" : "test address",
                    "company_phone" : "25252525",   
                    "administrator" : 1,
                })
        url = reverse('company_list_view')
        response = self.client.post(url, data=data, content_type='application/json')
        self.assertEqual(response.status_code, 201)
       
        invalid_data = json.dumps({
                   "id" : 4,
                    "company_zipcode" : "12345678901234567890",
                    "company_mail" : "testtestes",
                    "company_phone" : "151551515",  

                })
        url = reverse('company_list_view')
        response = self.client.post(url, data=invalid_data, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        masage = response._container[0]
        self.assertEqual(masage, 'Invalid input data. Please edit and try again.')

        self.client = Client()
        self.client.login(username="test@test.com", password="password")
        response = self.client.post(url, data=data, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        masage = response._container[0]
        self.assertEqual(masage, 'Permission denied')
        

    def test_put(self):
        data = json.dumps({
                   "id" : 1,
                    "company_zipcode" : "12344441",
                    "company_logo" : "http://test.tst",
                    "company_name" : "testcompany3",
                    "company_mail" : "test@test.com",
                    "company_address" : "test address",
                    "company_phone" : "25252525",   
                    "administrator" : 1,
                })


        data_with_dict = json.dumps({
                   "id" : 2,
                    "company_zipcode" : "12344441",
                    "company_logo" : "http://teest.tst",
                    "company_name" : "testcompany dict",
                    "company_mail" : "test@mail.com",
                    "company_address" : "test address dict",
                    "company_phone" : "2525255525",   
                    "administrator" : {"id" : 3, "id_company" : 2, "user" : 4},
                })

        url = reverse('company_details_view', args=[1])
        url_2 = reverse('company_details_view', args=[2])
        response = self.client.put(url, data=data, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response = self.client.put(url_2, data=data_with_dict, content_type='application/json')
        self.assertEqual(response.status_code, 201)
       
        invalid_data = json.dumps({
                   "id" : 1,
                    "company_zipcode" : "123456789012345678900",
                    "company_logo" : "http://test.tst",
                    "company_name" : "testcompany3",
                    "company_mail" : "testtestes",
                    "company_address" : "test address",
                    "company_phone" : "151551515",    
                    "administrator" : 2,
                })
        response = self.client.put(url, data=invalid_data, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        masage = response._container[0]
        self.assertEqual(masage, 'Invalid input data. Please edit and try again.')

        self.client = Client()
        self.client.login(username="test@test.com", password="password")
        data_user_1 = json.dumps({
                   "id" : 1,
                    "company_zipcode" : "123444411",
                    "company_logo" : "http://test.tst",
                    "company_name" : "testcompany1",
                    "company_mail" : "test@test.com",
                    "company_address" : "test address",
                    "company_phone" : "25252525",   
                    "administrator" : 1,
                })
        data_user_2 = json.dumps({
                   "id" : 2,
                    "company_zipcode" : "123444411",
                    "company_logo" : "http://teeest.tst",
                    "company_name" : "testcompany 2",
                    "company_mail" : "test@mail.test",
                    "company_address" : "test address 2",
                    "company_phone" : "252525552522",   
                    "administrator" : 3,
                })
        response = self.client.put(url, data=data_user_1, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        masage = response._container[0]
        self.assertEqual(masage, 'Permission denied')
        response = self.client.put(url_2, data=data_user_2, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        masage = response._container[0]
        self.assertEqual(masage, 'Permission denied')

    def test_delete(self):
        url = reverse('company_details_view', args=[1])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 201) 

        self.client = Client()
        self.client.login(username="test@test.com", password="password")
        url_2 = reverse('company_details_view', args=[2])
        response = self.client.delete(url_2)
        self.assertEqual(response.status_code, 400)
        masage = response._container[0]
        self.assertEqual(masage, 'Permission denied')