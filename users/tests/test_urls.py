from django.test import Client, TestCase
from django.urls import reverse, resolve
from users.views import IndexView, LoginToSite, LogOut, RegistrationOnSite, HomeView, EditProfile


# pytest --cov-report html --cov=./

class TestUsersUrls(TestCase):
    def test_index_url_resolve(self):
        client = Client()
        response = client.get('')
        assert response.status_code == 200
        # self.assertEqual(resolve(url).func.view_class, IndexView)
