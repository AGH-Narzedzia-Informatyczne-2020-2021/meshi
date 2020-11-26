from django.test import TestCase
from recipes.models import Recipe


class test_recipe_title(TestCase):
    def test_title_label(self):
        """This function checks if the object has title field"""
        recipe = Recipe.objects.get(id=1)
        field_label = Recipe._meta.get_field("title").verbose_name
        self.assertEqual(field_label, "title")

    def test_title_content(self):
        """This function checks if the object's title isn't Null"""
        recipe = Recipe.objects.get(id=1)
        field_object = Recipe._meta.get_field("title")
        content = field_object.value_from_object(recipe)
        self.assertNotEqual(content, None)

    def test_title_max_length(self):
        """This function checks object's title max length"""
        recipe = Recipe.objects.get(id=1)
        max_length = Recipe._meta.get_field("title").max_length
        self.assertEqual(max_length, 256)

    def test_title_length(self):
        """This function checks object's title max length"""
        recipe = Recipe.objects.get(id=1)
        field_object = Recipe._meta.get_field("title")
        content = field_object.value_from_object(recipe)
        title_length = len(content)
        score = 0
        if title_length < 256:
            score = 1
        self.assertEqual(score, 1)


class test_recipe_instructions(TestCase):
    def test_instruction_label(self):
        """This function checks if the object has instruction field"""
        recipe = Recipe.objects.get(id=1)
        field_label = Recipe._meta.get_field("instruction").verbose_name
        self.assertEqual(field_label, "instruction")

    def test_instruction_content(self):
        """This function checks if the object's instruction isn't Null"""
        recipe = Recipe.objects.get(id=1)
        field_object = Recipe._meta.get_field("instruction")
        content = field_object.value_from_object(recipe)
        self.assertNotEqual(content, None)


class test_recipe_image(TestCase):
    def test_image_url_label(self):
        """This function checks if the object has image field"""
        recipe = Recipe.objects.get(id=1)
        field_label = Recipe._meta.get_field("image").verbose_name
        self.assertEqual(field_label, "image")


class test_recipe_ease_of_prep(TestCase):
    def test_image_url_label(self):
        """This function checks if the object has ease_of_prep field"""
        recipe = Recipe.objects.get(id=1)
        field_label = Recipe._meta.get_field("ease_of_prep").verbose_name
        self.assertEqual(field_label, "ease_of_prep")

    def test_ease_of_prep_number(self):
        """This function checks if the object's ease_of_prep is integer number"""
        recipe = Recipe.objects.get(id=1)
        field_object = Recipe._meta.get_field("ease_of_prep")
        self.assertIsInstance(field_object, int)

    def test_ease_of_prep_value(self):
        """This function checks if the object's ease_of_prep is more then 1 and less then 10"""
        recipe = Recipe.objects.get(id=1)
        field_object = Recipe._meta.get_field("ease_of_prep")
        a = field_object.value_from_object(recipe)
        b = 1
        if a < 1:
            b = 0
        if a > 10:
            b = 0
        self.assertEqual(b, 1)


class test_recipe_rating(TestCase):
    def test_image_url_label(self):
        """This function checks if the object has rating field"""
        recipe = Recipe.objects.get(id=1)
        field_label = Recipe._meta.get_field("rating").verbose_name
        self.assertEqual(field_label, "rating")

    def test_ease_of_prep_number(self):
        """This function checks if the object's rating is integer number"""
        recipe = Recipe.objects.get(id=1)
        field_object = Recipe._meta.get_field("rating")
        a = type(field_object)
        self.assertEqual(a, "<class 'int'>")

    def test_ease_of_prep_value(self):
        """This function checks if the object's rating is more then 1 and less then 10"""
        recipe = Recipe.objects.get(id=1)
        field_object = Recipe._meta.get_field("rating")
        a = field_object.value_from_object(recipe)
        b = 1
        if a < 1:
            b = 0
        if a > 10:
            b = 0
        self.assertEqual(b, 1)


class test_recipe_prep_time(TestCase):
    def test_prep_time_label(self):
        """This function checks if the object has prep_time field"""
        recipe = Recipe.objects.get(id=1)
        field_label = Recipe._meta.get_field("prep_time").verbose_name
        self.assertEqual(field_label, "prep_time")

    def test_prep_time_number(self):
        """This function checks if the object's prep_time is integer number"""
        recipe = Recipe.objects.get(id=1)
        field_object = Recipe._meta.get_field("prep_time")
        a = type(field_object)
        self.assertEqual(a, "<class 'int'>")

    def test_prep_time_value(self):
        """This function checks if the object's rating is more then 1"""
        recipe = Recipe.objects.get(id=1)
        field_object = Recipe._meta.get_field("prep_time")
        a = field_object.value_from_object(recipe)
        b = 1
        if a < 1:
            b = 0
        self.assertEqual(b, 1)


# notes
# type
# id
