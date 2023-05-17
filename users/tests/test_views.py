from django.test import Client


class TestViews:
    def test_index(self):
        client = Client()
        response = client.get('')
        assert response.status_code == 200

    def test_login(self):
        client = Client()
        response = client.get('/login')
        assert response.status_code == 200

    def test_registration(self):
        client = Client()
        response = client.get('/registration')
        assert response.status_code == 200
