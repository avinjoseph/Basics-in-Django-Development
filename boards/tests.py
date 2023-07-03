from django.test import TestCase
from django.urls import reverse, resolve
from .views import home,board_topics
from .models import Board
# Create your tests here.

class HomeTests(TestCase):
    def setUp(self) -> None:
        self.board = Board.objects.create(name='Django',description='Django Board')
        url = reverse('home')
        self.response = self.client.get(url)    

    def test_home_view_status_code(self):
        self.assertEquals(self.response.status_code,200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func,home)

    def test_home_view_contains_link_to_topic_page(self):
        board_topics_url = reverse('board_topics',kwargs={'pk':self.board.pk})
        self.assertContains(self.response, 'href="{0}"'.format(board_topics_url))


class BoardTopictests(TestCase):
    def setUp(self) -> None:
        Board.objects.create(name='Django',description='Django Board')

    def test_board_topics_view_success_status_code(self):
        url = reverse('board_topics',kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code,200)

    def test_board_topics_views_not_found_status_code(self):
        url = reverse('board_topics', kwargs={'pk':99})
        response = self.client.get(url)
        self.assertEquals(response.status_code,404)

    def test_board_topics_url_resolves_board_topics_view(self):
        view = resolve('/boards/1/')
        self.assertEquals(view.func,board_topics)

    def test_board_topics_view_contains_link_back_to_homepage(self):
        board_topics_url = reverse('board_topics',kwargs={'pk':1})
        response = self.client.get(board_topics_url)
        homepage_url = reverse('home')
        self.assertContains(response,'href="{0}"'.format(homepage_url))

