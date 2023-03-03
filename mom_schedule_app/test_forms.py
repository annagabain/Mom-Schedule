from django.test import TestCase
from .forms import NewUserForm


class Test_NewUserForm(TestCase):

    def test_item_username_is_required(self):
        form = NewUserForm({'username': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors.keys())
        self.assertEqual(form.errors['username'][0], 'This field is required.')  # noqa

    def test_item_email_is_required(self):
        form = NewUserForm({'email': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0], 'This field is required.')  # noqa

    def test_item_password1_is_required(self):
        form = NewUserForm({'password1': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('password1', form.errors.keys())
        self.assertEqual(form.errors['password1'][0], 'This field is required.')  # noqa

    def test_item_password2_is_required(self):
        form = NewUserForm({'password2': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors.keys())
        self.assertEqual(form.errors['password2'][0], 'This field is required.')  # noqa

    def test_fields_are_explicit_in_form_metaclass(self):
        form = NewUserForm()
        self.assertEqual(form.Meta.fields, ("username", "email", "password1", "password2"))  # noqa
