import unittest
from django.test import RequestFactory
from django.urls import reverse
from .views import *

class TestViews(unittest.TestCase):
    def setUp(self):
        # Create a RequestFactory instance
        self.factory = RequestFactory()

    def test_login(self):
        request = self.factory.get(reverse('car_services/login'))
        response = login(request)
        self.assertEqual(response.status_code, 302)

    def test_callback(self):
        request = self.factory.get(reverse('car_services/callback'))
        response = callback(request)
        self.assertEqual(response.status_code, 302)

    def test_logout(self):
        request = self.factory.get(reverse('car_services/logout'))
        response = logout(request)
        self.assertEqual(response.status_code, 302)

    def test_index(self):
        request = self.factory.get(reverse('car_services/'))
        response = index(request)
        self.assertEqual(response.status_code, 200)

    def test_home(self):
        request = self.factory.get(reverse('car_services/home'))
        response = home(request)
        self.assertEqual(response.status_code, 200)

    def test_Dashboard(self):
        request = self.factory.get(reverse('car_services/Dashboard'))
        response = Dashboard(request)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()


class TestAPIViews(unittest.TestCase):
    def setUp(self):
        # Create a RequestFactory instance
        self.factory = RequestFactory()

    def test_LoadUserAPIView_get(self):
        request = self.factory.get(reverse('car_services/user'))
        response = LoadUserAPIView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_LoadUserAPIView_post(self):
        request = self.factory.post(reverse('car_services/user'), data={})
        response = LoadUserAPIView.as_view()(request)
        self.assertEqual(response.status_code, 201)

    # Add similar tests for other API views...

if __name__ == '__main__':
    unittest.main()
