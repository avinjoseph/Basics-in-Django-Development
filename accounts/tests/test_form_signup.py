from django.test import TestCase
from ..forms import SignUpForms

class SignUpFormTests(TestCase):
    def test_form_have_fields(self):
        form = SignUpForms()
        expexted = ['username','email','password1','password2']
        actual = list(form.fields)
        self.assertSequenceEqual(expexted,actual)