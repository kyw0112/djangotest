from django.test import TestCase
import json
from django.contrib.auth.models import User
from django.urls import reverse


class LMSTests(TestCase):
    def test_index_view(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "LMS API Overview")

    def test_swagger_view(self):
        response = self.client.get("/swagger/")
        self.assertEqual(response.status_code, 200)

    def test_signup_login_and_students(self):
        signup_resp = self.client.post('/api/auth/signup',
            data=json.dumps({'username': 'alice', 'password': 'pw'}),
            content_type='application/json')
        self.assertEqual(signup_resp.status_code, 200)

        login_resp = self.client.post('/api/auth/login',
            data=json.dumps({'username': 'alice', 'password': 'pw'}),
            content_type='application/json')
        self.assertEqual(login_resp.status_code, 200)

        # create student
        self.client.force_login(User.objects.get(username='alice'))
        create_resp = self.client.post('/api/students/',
            data=json.dumps({'name': 'John', 'contact': '010-1234-5678'}),
            content_type='application/json')
        self.assertEqual(create_resp.status_code, 200)

        list_resp = self.client.get('/api/students/')
        self.assertEqual(list_resp.status_code, 200)
        self.assertContains(list_resp, 'John')
