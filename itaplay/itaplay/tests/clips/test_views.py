import json

from django.test import Client
from django.test import TestCase
from django.contrib.auth.models import User
from clips.models import Clip
from clips.views import ClipView
from authentication.models import AdviserUser
from django.core.urlresolvers import reverse

class ClipViewTestCase(TestCase):

    def setUp(self):
        
        Clip.objects.create(
            id=1,
            name="clip",
            description="descr",
            url="http://test.test/video.mp4",
            mimetype="video/mp4",
        )
        
        Clip.objects.create(
            id=2,
            name="cliptwo",
            description="descrtwo",
            url="http://test.test/image.jpeg",
            mimetype="image/jpeg",
        )

        Clip.objects.create(
            id=3,
            name="clip3",
            description="descr3",
            url="http://test.test/image.pdf",
            mimetype="application/pdf",
        )


        User.objects.create(
            username="test@test.com",
            email="test@test.com",
            id=1
        )

        user = User.objects.get(id=1)
        user.set_password("password")
        user.save()
        
        self.client = Client()
        self.client.login(username="test@test.com", password="password")

    def test_delete_clip(self):
        url = reverse('clip_delete', args=[1])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 201)

    def test_get_all_clips(self):
        url = reverse('clips')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_get_clip(self):
        url = reverse('get_clip', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

