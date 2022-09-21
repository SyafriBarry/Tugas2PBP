from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class HomepageTests(TestCase):
    def testHTML(self):
        response = self.client.get("/mywatchlist/html/")
        self.assertEqual(response.status_code, 200)
        
    def testJson(self):
        response = self.client.get("/mywatchlist/json/")
        self.assertEqual(response.status_code, 200)
        
    def testXML(self):
        response = self.client.get("/mywatchlist/xml/")
        self.assertEqual(response.status_code, 200)    
