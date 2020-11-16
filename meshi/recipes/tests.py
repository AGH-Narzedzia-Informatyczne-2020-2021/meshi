from django.test import TestCase
from catalog.models import Author

# Create your tests here.


class RecipeModelTest(TestCase):

    def setUpTestData(cls):
        recipe.objects.create()
        
#title
    def test_title_content(self):
        recipe = Recipe.objects.get(id=1)
        field_label = recipe._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_title_length(self):
        recipe = Recipe.objects.get(id=1)
        max_length = recipe._meta.get_field('title').max_length
        self.assertEqual(max_length, 250)
        
#notes
    def test_title_content(self):
        recipe = Recipe.objects.get(id=1)
        field_label = recipe._meta.get_field('notes').verbose_name
        self.assertEqual(field_label, 'notes')

    def test_title_length(self):
        recipe = Recipe.objects.get(id=1)
        max_length = recipe._meta.get_field('notes').max_length
        self.assertEqual(max_length, 250)
        
#types
    def test_title_content(self):
        recipe = Recipe.objects.get(id=1)
        field_label = recipe._meta.get_field('types').verbose_name
        self.assertEqual(field_label, 'types')

    def test_title_length(self):
        recipe = Recipe.objects.get(id=1)
        max_length = recipe._meta.get_field('types').max_length
        self.assertEqual(max_length, 250)


