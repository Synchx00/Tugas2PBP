from django.test import TestCase
from django.urls import reverse, resolve
from mywatchlist.views import show_film_list, show_xml, show_json

# Create your tests here.
class TestUrls(TestCase):

    def setUp(self):
        self.urlToViewHtml = reverse(
            'mywatchlist:show_film_list'
        )
        self.urlToViewJson = reverse(
            'mywatchlist:show_json'
        )
        self.urlToViewXML = reverse(
            'mywatchlist:show_xml'
        )

    def test_mywatchlist_urls_resolve(self):
        self.assertEqual(
            resolve(
                self.urlToViewHtml
            ).func,
            show_film_list
        )
        
    def test_mywatchlist_json_resolve(self):
        self.assertEqual(
            resolve(
                self.urlToViewJson
            ).func,
            show_json
        )

    def test_mywatchlist_xml_resolve(self):
        self.assertEqual(
            resolve(
                self.urlToViewXML
            ).func,
            show_xml
        )