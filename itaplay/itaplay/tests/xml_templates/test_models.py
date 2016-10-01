"""This module has tests for XmlTemplate Models"""
from django.test import TestCase
from xml_templates.models import XmlTemplate


class XmlTemplateModelTests(TestCase):
    """This class tests XmlTemplate Models"""

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
        """Ensures that unicode representaton of xml template works correct"""
        xmlTemplate = XmlTemplate.objects.get(template_name="template1")
        self.assertEqual(
            unicode(xmlTemplate),
            u'template1')

    def test_xml_template_get_by_id(self):
        """Ensures xml template can be retrieved by id"""
        xmlTemplateExpected = XmlTemplate.objects.get(id=1)
        self.assertEqual(XmlTemplate.get_by_id(1), xmlTemplateExpected)

    def test_xml_template_get_all(self):
        """Tests retrivieng all xml templates"""
        xmlTemplatesExpected = XmlTemplate.objects.all()
        self.assertItemsEqual(XmlTemplate.get_all(), xmlTemplatesExpected)

    def test_xml_template_set(self):
        """Tests setting xml template"""
        xmlTemplateResult = XmlTemplate.objects.get(id=1)
        xmlTemplateResult.set("newTemplate", '''<?xml >
            <project name="newTemplate">
            </project> ''',)
        self.assertEqual(xmlTemplateResult.template_name, "newTemplate")
        self.assertEqual(xmlTemplateResult.template_content, '''<?xml >
            <project name="newTemplate">
            </project> ''')

    def test_xml_template_delete(self):
        """Tests deleting xml template"""
        XmlTemplate.delete(1)
        self.assertEqual(XmlTemplate.objects.count(), 1)
        self.assertFalse(XmlTemplate.objects.filter(pk=1).exists())
