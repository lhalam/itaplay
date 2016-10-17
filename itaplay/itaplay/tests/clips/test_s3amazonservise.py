# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from utils.amazons3service import save_on_amazon_with_boto, delete_from_amazon_with_boto
from django.core.files import File


class AmazonTestCase(TestCase):

    def test_delete_from_amazon_with_boto(self):
        url = 'https://itaplayadviserireland.s3.amazonaws.com/media/Logo.png'
        delete_file = delete_from_amazon_with_boto(url)
        self.assertEqual(delete_file, True)

