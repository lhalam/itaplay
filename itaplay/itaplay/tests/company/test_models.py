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
            company_zipcode="79008",
            company_logo="http://test.test",
            company_name="testcompany",
            company_mail="test@test.test",
            company_address= "testaddress",
            company_phone="+380901234567",      
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
            company_zipcode="794508",
            company_logo="http://test2.test",
            company_name="testcompany2",
            company_mail="test2@test.test",
            company_address= "testaddress2",
            company_phone="+380901234677",
            administrator=AdviserUser.objects.get(id=2)
        )


    def test_company_get_by_name(self):
        """"""
        company = Company.objects.get(company_name="testcompany")
        self.assertEqual(company.company_name, "testcompany")
        self.assertEqual(company.company_phone, "+380901234567")

    def test_company_get_by_zipcode_local(self):
        Company.objects.create(
            id=3,
            company_zipcode="79007",
            company_logo="2132",
            company_name="testcompany1",
            company_mail="test@test.test1",
            company_address= "testaddress3",
            company_phone="+3809012345671",
        )

        company = Company.objects.get(company_zipcode="79007")
        self.assertEqual(company.company_logo, "2132")
    
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
            company_zipcode="379007",
            company_logo="332132",
            company_name="testcompany3",
            company_mail="test@test.test3",
            company_address= "testaddress3",
            company_phone="+3809012345673",
        )
        
        self.assertEqual(len(Company.get_company()), 3)
        Company().delete_company(3)
        self.assertEqual(len(Company.get_company()), 2)

    def test_set_company_create(self):
        admin = AdviserUser.objects.get(id=1)
        data = {
                   "id" : 3,
                    "company_zipcode" : "379007",
                    "company_logo" : "32132",
                    "company_name" : "testcompany3",
                    "company_mail" : "test@test.test3",
                    "company_address" : "testaddress3",
                    "company_phone" : "+380951234567",   
                    "administrator" : admin,
                }
        Company().set_company(data)
        company = Company.get_company(3)
        self.assertEqual(company.company_name, "testcompany3")
        self.assertEqual(company.company_mail, "test@test.test3")
        self.assertEqual(company.company_phone, "+380951234567")
        self.assertEqual(company.company_zipcode, "379007")
                
    def test_set_company_update(self):
        admin = AdviserUser.objects.get(id=1)
        data = {
                   "id" : 1,
                    "company_zipcode" : "379007",
                    "company_logo" : "32132",
                    "company_name" : "testcompany1",
                    "company_mail" : "test@test.test1",
                    "company_address" : "testaddress1",
                    "company_phone" : "+380951234567",   
                    "administrator" : admin,
                }
        
        company = Company.get_company(1)
        company.set_company(data)
        company = Company.get_company(1)
        self.assertEqual(company.company_name, "testcompany1")
        self.assertEqual(company.company_mail, "test@test.test1")
        self.assertEqual(company.company_phone, "+380951234567")
        self.assertEqual(company.company_zipcode, "379007")
        self.assertEqual(company.administrator, admin)
                            