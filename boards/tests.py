from django.urls import reverse
from django.urls import resolve
from django.test import TestCase
from .views import home, saint_page
from .models import Saint

class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)
        
class BoardTopicsTests(TestCase):
    def setUp(self):
        Saint.objects.create(name='Name', description='Catholic Saint')

    def test_board_topics_view_success_status_code(self):
        url = reverse('saint_page', kwargs={'id': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_board_topics_view_not_found_status_code(self):
        url = reverse('saint_page', kwargs={'id': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_board_topics_url_resolves_board_topics_view(self):
        view = resolve('/saints/1/')
        self.assertEquals(view.func, saint_page)