from django.test import TestCase
from django.shortcuts import resolve_url as r


class HomeTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('home'))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'index.html')

    def test_html_has_svcpa_symbol(self):
        """index.html must have SVCPA symbol"""
        expected = 'img/logoSVCPA1_menor.jpg'
        self.assertContains(self.resp, expected)