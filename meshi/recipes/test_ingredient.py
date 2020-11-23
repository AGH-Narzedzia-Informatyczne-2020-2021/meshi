from django.test import TestCase
from recipes.models import Ingredient

class test_ingredient_name(TestCase):
    def test_name_label(self):
        """This function checks if the object has name field"""
        ingredient = Ingredient.objects.get(id=1)
        field_label = Ingredient._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_name_content(self):
        """This function checks if the object's name isn't Null"""
        ingredient = Ingredient.objects.get(id=1)
        field_object = Ingredient._meta.get_field('name')
        content = field_object.value_from_object(ingredient)
        self.assertNotEqual(content, Null)

    def test_name_max_length(self):
        """This function checks object's name max length"""
        ingredient = Ingredient.objects.get(id=1)
        max_length = Ingredient._meta.get_field('name').max_length
        self.assertEqual(max_length, 128)
    
    def test_title_length(self):
        """This function checks object's name max length"""
        ingredient = Ingredient.objects.get(id=1)
        field_object = Ingredient._meta.get_field('name')
        content = field_object.value_from_object(ingredient)
        title_length=len(content)
        score = 0
        if title_length < 128 :
            score=1
        self.assertEqual(score, 1)