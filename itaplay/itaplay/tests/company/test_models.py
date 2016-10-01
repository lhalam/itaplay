from django.test import TestCase
from company.models import Company


class AnimalTestCase(TestCase):

    def setUp(self):
        Company.objects.create(
            company_zipcode="79008",
            company_logo="http://test.test",
            company_name="testcompany",
            company_mail="test@test.test",
            company_phone="+380901234567",
        )
        pass

    def test_company_get_by_name(self):
        """"""
        company = Company.objects.get(company_name="testcompany")
        self.assertEqual(company.company_name, "testcompany")
        self.assertEqual(company.company_phone, "+380901234567")

    def test_company_get_by_zipcode_local(self):
        Company.objects.create(
            company_zipcode="79007",
            company_logo="2132",
            company_name="testcompany1",
            company_mail="test@test.test1",
            company_phone="+3809012345671",
        )

        company = Company.objects.get(company_zipcode="79007")
        self.assertEqual(company.company_logo, "2132")
        # self.assertEqual(company.company_phone, "+380901234567")
