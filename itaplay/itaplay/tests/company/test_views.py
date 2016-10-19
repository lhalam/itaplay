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
            zipcode="79008",
            logo="http://test.test",
            name="testcompany",
            mail="test@test.test",
            address= "testaddress",
            phone="+380901234567",      
        )

        Company.objects.create(
            id=2,
            zipcode="794508",
            logo="http://test2.test",
            name="testcompany2",
            mail="test2@test.test",
            address= "testaddress2",
            phone="+380901234677",
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
        
        company = Company.get_company(1)
        company.administrator = AdviserUser.objects.get(id=1)
        company.save()

        self.client = Client()
        self.client.login(username="test@superadmin.com", password="password")

    def test_get_list_superadmin(self):
        url = reverse('company_list_view')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_get_list_company_user(self):  
        self.client = Client()
        self.client.login(username="test@test.com", password="password")
        url = reverse('company_list_view') 
        response = self.client.get(url)
        company = json.loads(response._container[0])[0]
        self.assertEqual(company.get("id"), 1)
        self.assertEqual(response.status_code, 200)
    

    def test_get_object_superadmin(self):
        url = reverse('company_details_view', args=[1])
        response = self.client.get(url)
        company = json.loads(response._container[0])["company"]
        self.assertEqual(company.get("id"), 1)
        self.assertEqual(response.status_code, 200)

    def test_get_object_company_user(self):   
        self.client = Client()
        self.client.login(username="test@test.com", password="password")
        url = reverse('company_details_view', args=[1])
        response = self.client.get(url)
        company = json.loads(response._container[0])["company"]
        self.assertEqual(company.get("id"), 1)
        self.assertEqual(response.status_code, 200)

    def test_get_object_company_user_try_foreign_company(self):
        self.client = Client()
        self.client.login(username="test@test.com", password="password")
        url = reverse('company_details_view', args=[2])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 400)
        massage = response._container[0]
        self.assertEqual(massage, 'Permission denied')
        

    def test_post_superadmin(self):
        data = json.dumps({
                    "id" : 3,
                    "zipcode" : "12344441",
                    "logo" : "http://test.tst",
                    "name" : "testcompany3",
                    "mail" : "test@test.com",
                    "address" : "test address",
                    "phone" : "25252525",  
                })
        url = reverse('company_list_view')
        response = self.client.post(url, data=data, content_type='application/json')
        self.assertEqual(response.status_code, 201)
    
    def test_post_invalid_data(self):   
        invalid_data = json.dumps({
                    "id" : 4,
                    "zipcode" : "12345678901234567890",
                    "mail" : "testtestes",
                    "phone" : "151551515",  

                })
        url = reverse('company_list_view')
        response = self.client.post(url, data=invalid_data, content_type='application/json')
        self.assertEqual(response.status_code, 400)
    
    def test_post_company_user(self):
        self.client = Client()
        self.client.login(username="test@test.com", password="password")
        url = reverse('company_list_view')
        data = json.dumps({
                    "id" : 4,
                    "zipcode" : "123444414",
                    "logo" : "http://testtest.tst",
                    "name" : "testcompany4",
                    "mail" : "test4@test.com",
                    "address" : "test 4address",
                    "phone" : "252525254",   
                })
        response = self.client.post(url, data=data, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        massage = response._container[0]
        self.assertEqual(massage, 'Permission denied')
        

    def test_put_superadmin(self):
        data = json.dumps({
                   "id" : 2,
                    "zipcode" : "12344441",
                    "logo" : "http://teest.tst",
                    "name" : "testcompany dict",
                    "mail" : "test@mail.com",
                    "address" : "test address dict",
                    "phone" : "2525255525",   
                    "administrator" : {"id" : 3, "id_company" : 2, "user" : 4},
                })

        url = reverse('company_details_view', args=[2])
        response = self.client.put(url, data=data, content_type='application/json')
        self.assertEqual(response.status_code, 201)
    
    def test_put_invalid_data(self):
        invalid_data = json.dumps({
                   "id" : 1,
                    "zipcode" : "123456789012345678900",
                    "logo" : "http://test.tst",
                    "name" : "testcompany3",
                    "mail" : "testtestes",
                    "address" : "test address",
                    "phone" : "151551515",    
                    "administrator" : {"id" : 1, "id_company" : 1, "user" : 2},
                })
        url = reverse('company_details_view', args=[1])
        response = self.client.put(url, data=invalid_data, content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_put_comapny_admin(self):
        self.client = Client()
        self.client.login(username="test@test.com", password="password")
        data = json.dumps({
                    "id" : 1,
                    "zipcode" : "123444411",
                    "logo" : "http://test.tst",
                    "name" : "testcompany1",
                    "mail" : "test@test.com",
                    "address" : "test address",
                    "phone" : "25252525",   
                    "administrator" : {"id" : 1, "id_company" : 1, "user" : 2},
                })
        url = reverse('company_details_view', args=[1])
        response = self.client.put(url, data=data, content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_put_admin_comapny_try_foreign_company(self): 
        self.client = Client()
        self.client.login(username="test@test.com", password="password")   
        data = json.dumps({
                    "id" : 2,
                    "zipcode" : "123444411",
                    "logo" : "http://teeest.tst",
                    "name" : "testcompany 2",
                    "mail" : "test@mail.test",
                    "address" : "test address 2",
                    "phone" : "252525552522",   
                    "administrator" : {"id" : 3, "id_company" : 2, "user" : 4},
                })
        url = reverse('company_details_view', args=[2])
        response = self.client.put(url, data=data, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        massage = response._container[0]
        self.assertEqual(massage, 'Permission denied')

    def test_put_comapny_user(self): 
        self.client = Client()
        self.client.login(username="test3@test.com", password="password")
        data_regular_user = json.dumps({
                    "id" : 1,
                    "zipcode" : "123444411",
                    "logo" : "http://teeest.tst",
                    "name" : "testcompany 2",
                    "mail" : "test@mail.test",
                    "address" : "test address 2",
                    "phone" : "252525552522",   
                    "administrator" : {"id" : 1, "id_company" : 1, "user" : 2},
                })
        url = reverse('company_details_view', args=[1])
        response = self.client.put(url, data=data_regular_user, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        massage = response._container[0]
        self.assertEqual(massage, 'Permission denied')

    def test_delete_superadmin(self):
        url = reverse('company_details_view', args=[1])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 201) 
    
    def test_delete_company_user(self):
        self.client = Client()
        self.client.login(username="test@test.com", password="password")
        url = reverse('company_details_view', args=[2])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 400)
        massage = response._container[0]
        self.assertEqual(massage, 'Permission denied')