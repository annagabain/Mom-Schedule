from django.test import TestCase
from .forms import NewUserForm


class Test_NewUserForm(TestCase):

    def test_item_username_is_required(self):
        form = NewUserForm({'username': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors.keys())
        self.assertEqual(form.errors['username'][0], 'This field is required.')
