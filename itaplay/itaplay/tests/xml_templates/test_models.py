from django.test import TestCase
from xml_templates.models import XmlTemplate


class XmlTemplateModelTests(TestCase):

    def setUp(self):
        XmlTemplate.objects.create(
            id=1,
            template_name='template1',
            template_content='''<?xml >
            <project name="template1">
            </project> ''',
        )
        XmlTemplate.objects.create(
            id=2,
            template_name='template2',
            template_content='''<?xml >
            <project name="template2">
            </project> ''',
        )

    def test_unicode_xml_template(self):
        xmlTemplate = XmlTemplate.objects.get(template_name="template1")
        self.assertEqual(
            unicode(xmlTemplate),
            u'template1')

    def test_xml_template_get_by_id(self):
        xmlTemplateExpected = XmlTemplate.objects.get(id=1)
        self.assertEquals(XmlTemplate.get_by_id(1), xmlTemplateExpected)

    def test_xml_template_get_all(self):
        xmlTemplatesExpected = XmlTemplate.objects.all()
        self.assertItemsEqual(XmlTemplate.get_all(), xmlTemplatesExpected)

    def test_xml_template_set(self):
        xmlTemplateResult = XmlTemplate.objects.get(id=1)
        xmlTemplateResult.set("newTemplate", '''<?xml >
            <project name="newTemplate">
            </project> ''',)
        self.assertEquals(xmlTemplateResult.template_name, "newTemplate")
        self.assertEquals(xmlTemplateResult.template_content, '''<?xml >
            <project name="newTemplate">
            </project> ''')

    def test_xml_template_delete(self):
        XmlTemplate.delete(1)
        self.assertEquals(XmlTemplate.objects.count(), 1)
        self.assertFalse(XmlTemplate.objects.filter(pk=1).exists())
