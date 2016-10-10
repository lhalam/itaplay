from django.test import TestCase
from company.models import Company
from django.contrib.auth.models import User
from authentication.models import AdviserUser


class CompanyTestCase(TestCase):

    def setUp(self):

        User.objects.create(
            username="test@test.com",
            email="test@test.com",
            id=1
        )

        User.objects.create(
            username="test2@test.com",
            email="test2@test.com",
            id=2
        )

        user = User.objects.get(id=1)
        user.set_password("password")
        user.save()

        user = User.objects.get(id=2)
        user.set_password("password")
        user.save()
        
        Company.objects.create(
            id=1,
            zipcode="79008",
            logo="http://test.test",
            name="testcompany",
            mail="test@test.test",
            address="testaddress",
            phone="+380901234567",      
        )

        AdviserUser.objects.create(
            user=User.objects.get(id=1),
            id_company=Company.objects.get(id=1),
            id=1
        )
        
        AdviserUser.objects.create(
            user=User.objects.get(id=2),
            id_company=Company.objects.get(id=1),
            id=2
        )    

        Company.objects.create(
            id=2,
            zipcode="794508",
            logo="http://test2.test",
            name="testcompany2",
            mail="test2@test.test",
            address="testaddress2",
            phone="+380901234677",
            administrator=AdviserUser.objects.get(id=2)
        )


    def test_company_get_by_name(self):
        """"""
        company = Company.objects.get(name="testcompany")
        self.assertEqual(company.name, "testcompany")
        self.assertEqual(company.phone, "+380901234567")

    def test_company_get_by_zipcode_local(self):
        Company.objects.create(
            id=3,
            zipcode="79007",
            logo="2132",
            name="testcompany1",
            mail="test@test.test1",
            address="testaddress3",
            phone="+3809012345671",
        )

        company = Company.objects.get(zipcode="79007")
        self.assertEqual(company.logo, "2132")
    
    def test_get_company(self):
        companies = Company.get_company()
        company1 = Company.objects.get(id=1)
        company2 = Company.objects.get(id=2)
        self.assertEqual(companies[0], company1)
        self.assertEqual(companies[1], company2)

    def test_get_company_by_id(self):
        company = Company.get_company(1)
        company_id_1 = Company.objects.get(id=1)
        self.assertEqual(company, company_id_1)
    
    def test_delete_company(self):
        Company.objects.create(
            id=3,
            zipcode="379007",
            logo="332132",
            name="testcompany3",
            mail="test@test.test3",
            address= "testaddress3",
            phone="+3809012345673",
        )
        
        self.assertEqual(len(Company.get_company()), 3)
        Company().delete_company(3)
        self.assertEqual(len(Company.get_company()), 2)

    def test_set_company_create(self):
        admin = AdviserUser.objects.get(id=1)
        data = {
                   "id" : 3,
                    "zipcode" : "379007",
                    "logo" : "32132",
                    "name" : "testcompany3",
                    "mail" : "test@test.test3",
                    "address" : "testaddress3",
                    "phone" : "+380951234567",   
                    "administrator" : admin,
                }
        Company().set_company(data)
        company = Company.get_company(3)
        self.assertEqual(company.name, "testcompany3")
        self.assertEqual(company.mail, "test@test.test3")
        self.assertEqual(company.phone, "+380951234567")
        self.assertEqual(company.zipcode, "379007")
                
    def test_set_company_update(self):
        admin = AdviserUser.objects.get(id=1)
        data = {
                   "id" : 1,
                    "zipcode" : "379007",
                    "logo" : "32132",
                    "name" : "testcompany1",
                    "mail" : "test@test.test1",
                    "address" : "testaddress1",
                    "phone" : "+380951234567",   
                    "administrator" : admin,
                }
        
        company = Company.get_company(1)
        company.set_company(data)
        company = Company.get_company(1)
        self.assertEqual(company.name, "testcompany1")
        self.assertEqual(company.mail, "test@test.test1")
        self.assertEqual(company.phone, "+380951234567")
        self.assertEqual(company.zipcode, "379007")
        self.assertEqual(company.administrator, admin)
                            