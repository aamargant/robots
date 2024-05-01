from django.test import TestCase
from django.test import Client
from ..forms import robotsForm

class TestViews(TestCase):
    def test_render_homepage(self):
        c = Client()
        response = c.post("/", {})
        self.assertEqual(response.status_code, 200)
    
    def test_render_robots(self):
        c = Client()
        response = c.post("/robots/", {})
        self.assertEqual(response.status_code, 200)

    def test_render_robots_payload(self):
        payload = {
            "website": "https://www.capterra.com/",
        }
        c = Client()
        response = c.post("/robots/", payload)
        self.assertEqual(response.status_code, 200)
