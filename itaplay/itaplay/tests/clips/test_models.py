from django.test import TestCase
from clips.models import Clip
from django.core.exceptions import ValidationError
import json


class ClipTestCase(TestCase):

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

    def test_clip_get_by_name(self):
 
        clip = Clip.objects.get(name="clip")
        self.assertEqual(clip.name, "clip")

    def test_clip_get_by_url(self):

        clip = Clip.objects.get(name="cliptwo")
        self.assertEqual(clip.url, "http://test.test/image.jpeg")

    def test_get_all_clips(self):
        clips = Clip.get_all_clips()
        clip1 = Clip.objects.get(id=1)
        clip2 = Clip.objects.get(id=2)
        self.assertEqual(clips[0], clip1)
        self.assertEqual(clips[1], clip2)

    def test_get_clip_by_id(self):
        clip = Clip.get_clip(1)[0]
        type(clip)
        clip1 = Clip.objects.get(id=1)
        self.assertEqual(clip, clip1)

    def test_generate_video_mimetype(self):
        clip = Clip.objects.get(name="clip")
        mimetype = clip.generate_mimetype(clip.url)
        self.assertEqual(mimetype, 'video/mp4')

    def test_generate_image_mimetype(self):
        clip2 = Clip.objects.get(name="cliptwo")
        mimetype = clip2.generate_mimetype(clip2.url)
        self.assertEqual(mimetype, 'image/jpeg')

    def test_generate_validation_error_mimetype(self):
        with self.assertRaises(ValidationError):
            clip3 = Clip.objects.get(name="clip3")
            clip3.generate_mimetype(clip3.url)


