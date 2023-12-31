from django.test import TestCase
from django.urls import resolve, reverse
from django.contrib.admin import views as auth_views

class PasswordResetDoneView(TestCase):

    def setUp(self) -> None:
        url = reverse('password_reset_done')
        self.response = self.client.get(url)

    def test_status_code(self):
        self.assertEqual(self.response.status_code,200)

    def test_view_function(self):
        view = resolve('/reset/done/')
        self.assertEquals(view.func.view_class,auth_views.PasswordResetDoneView)
        