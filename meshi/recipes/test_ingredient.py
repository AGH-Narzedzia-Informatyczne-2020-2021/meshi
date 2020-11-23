from django.test import TestCase
from recipes.models import Ingredient

class test_recipe_title(TestCase)
{
    def test_title_content(self):
        field_label = recipe._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_title_length(self):
        recipe = Recipe.objects.get(id=1)
        max_length = recipe._meta.get_field('title').max_length
        self.assertEqual(max_length, 256)
}