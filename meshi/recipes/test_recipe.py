from django.test import TestCase
from recipes.models import Recipe

class test_recipe_title(TestCase):

    def setUp(self):
        """This function creates objects which will be testing"""
        Recipe.objects.create() #create object
        Recipe.objects.create() #create object
        Recipe.objects.create() #create object

    def test_title_label(self):
        """This function checks if the object has title field"""
        recipe = Recipe.objects.get(id=1)
        field_label = Recipe._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_title_content(self)
        """This function checks if the object's title isn't Null"""
        recipe = Recipe.objects.get(id=1)
        field_object = Recipe._meta.get_field('title')
        content = field_object.value_from_object(recipe)
        self.assertNotEqual(content, Null)

    def test_title_max_length(self):
        """This function checks object's title max length"""
        recipe = Recipe.objects.get(id=1)
        max_length = Recipe._meta.get_field('title').max_length
        self.assertEqual(max_length, 256)
    
    def test_title_length(self):
        """This function checks object's title max length"""
        recipe = Recipe.objects.get(id=1)
        field_object = Recipe._meta.get_field('title')
        content = field_object.value_from_object(recipe)
        title_length=len(content)
        score = 0
        if title_length < 256 :
            score=1
        self.assertEqual(score, 1)
        


class test_recipe_instructions(TestCase):

