from django.test import TestCase
from .models import *


class TestModels(TestCase):

    def test_item_string_method_returns_title(self):
        item = Task_Category.objects.create(name='Test Category Name')
        self.assertEqual(str(item), 'Test Category Name')
