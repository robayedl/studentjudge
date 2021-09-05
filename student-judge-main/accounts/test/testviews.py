from django.test import TestCase,Client
from django.urls import reverse


class TestViews(TestCase):
    def test_Login_get(self):
        client=Client()
        response=client.get(reverse('login'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'auth/login.html')

