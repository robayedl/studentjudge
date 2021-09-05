from django.test import SimpleTestCase
from django.urls import reverse, resolve
from accounts.views import LoginView,UpdateProfile

class TestUrls(SimpleTestCase):
    def test_Login_url_is_resolved(self):
        url=reverse('login')
        self.assertEqual(resolve(url).func,LoginView)
    def test_profile_url_is_resolved(self):
        url=reverse('profile')
        self.assertEqual(resolve(url).func,UpdateProfile)
