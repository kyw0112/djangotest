from django.test import TestCase
from django.urls import reverse


class LMSTests(TestCase):
    def test_index_view(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "LMS backend is running")

    def test_swagger_view(self):
        response = self.client.get("/swagger/")
        self.assertEqual(response.status_code, 200)
