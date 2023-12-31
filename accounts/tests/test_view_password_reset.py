from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.core import mail
from django.urls import reverse,resolve
from django.test import TestCase

class PasswordResetTests(TestCase):
    def setUp(self) -> None:
        url = reverse('password_reset')
        self.response = self.client.get(url)

    def test_view_function(self):
        self.assertEquals(self.response.status_code,200)

    def test_csrf_token(self):
        self.assertContains(self.response,'csrfmiddlewaretoken')

    def test_view_function(self):
        view = resolve('/reset/')
        self.assertEquals(view.func.view_class,auth_views.PasswordResetView)

    def test_contains_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form,PasswordResetForm)

    def test_form_inputs(self):
        self.assertContains(self.response,'<input',2)
        self.assertContains(self.response,'type="email"',1)

class SuccessfulPasswordResetTests(TestCase):
    def setUp(self) -> None:
        email = 'john@doe.com'
        User.objects.create_user(username='john',email=email,password='123abcdef')
        url = reverse('password_reset')
        self.response = self.client.post(url,{'email':email})

    def test_redirection(self):
        url = reverse('password_reset_done')
        self.assertRedirects(self.response,url)

    def test_send_password(self):
        self.assertEqual(1,len(mail.outbox))

class InvalidPasswordResetTests(TestCase):
    def setUp(self) -> None:
        url = reverse('password_reset')
        self.response = self.client.post(url,{'email':'donotexist@email.com'})

    def test_redirection(self):
        url = reverse('password_reset_done')
        self.assertRedirects(self.response,url)

    def test_no_reset_email_send(self):
        self.assertEqual(0,len(mail.outbox))

        
        