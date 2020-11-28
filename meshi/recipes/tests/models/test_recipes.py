from django.test import TestCase
from recipes.models import Recipe
from recipes.models import Ingredient
from django.db.models.fields import IntegerField


class RecipeTest(TestCase):
    def setUp(self):
        ingredient_1 = Ingredient.objects.create(
            id=1, name="1 cup Shredded Coconut"
        ).save()
        ingredient_2 = Ingredient.objects.create(id=2, name="eggs").save()
        ingredient_3 = Ingredient.objects.create(id=3, name="butter").save()
        recipe_1 = Recipe.objects.create(
            id=1,
            title="Maple-Sweetened Banana Muffins",
            instructions="Bring a pot of salted water to a boil.",
            image="",
            ease_of_prep="4",
            rating="10",
            prep_time="60",
            notes="""Coconut Carrot Easter Cake is the perfect, 
            sweet end to a traditional Easter brunch. 
            It has such a moist crumb, loads of flavor and a luscious frosting!""",
            types="",
        )
        recipe_1.ingredients.add(1, 2, 3)

    def test_recipe_title_label(self):
        """This function checks if the object has title field"""
        field_label = Recipe._meta.get_field("title").verbose_name
        self.assertEqual(field_label, "title")

    def test_recipe_title_content(self):
        """This function checks if the object's title isn't Null"""
        recipe = Recipe.objects.get(id=1)
        field_object = Recipe._meta.get_field("title")
        content = field_object.value_from_object(recipe)
        self.assertNotEqual(content, None)

    def test_recipe_title_max_length(self):
        """This function checks object's title max length"""
        recipe = Recipe.objects.get(id=1)
        max_length = Recipe._meta.get_field("title").max_length
        self.assertEqual(max_length, 256)

    def test_recipe_title_length(self):
        """This function checks object's title max length"""
        recipe = Recipe.objects.get(id=1)
        field_object = Recipe._meta.get_field("title")
        content = field_object.value_from_object(recipe)
        self.assertLessEqual(len(content), 256)

    def test_recipe_instruction_label(self):
        """This function checks if the object has instructions field"""
        field_label = Recipe._meta.get_field("instructions").verbose_name
        self.assertEqual(field_label, "instructions")

    def test_recipe_instruction_content(self):
        """This function checks if the object's instructions isn't Null"""
        recipe = Recipe.objects.get(id=1)
        field_object = Recipe._meta.get_field("instructions")
        content = field_object.value_from_object(recipe)
        self.assertNotEqual(content, None)

    def test_recipe_image_url_label(self):
        """This function checks if the object has image field"""
        field_label = Recipe._meta.get_field("image").verbose_name
        self.assertEqual(field_label, "image")

    def test_recipe_ease_of_prep_label(self):
        """This function checks if the object has ease_of_prep field"""
        field_label = Recipe._meta.get_field("ease_of_prep").verbose_name
        self.assertEqual(field_label, "ease of prep")

    def test_recipe_ease_of_prep_number(self):
        """This function checks if the object's ease_of_prep is integer number"""
        recipe = Recipe.objects.get(id=1)
        field_object = Recipe._meta.get_field("ease_of_prep")
        self.assertIsInstance(field_object, IntegerField)

    def test_recipe_ease_of_prep_value(self):
        """This function checks if the object's ease_of_prep is more then 1 and less then 10"""
        recipe = Recipe.objects.get(id=1)
        field_object = Recipe._meta.get_field("ease_of_prep")
        self.assertLessEqual(field_object.value_from_object(recipe), 10)
        self.assertGreaterEqual(field_object.value_from_object(recipe), 1)

    def test_recipe_rating_label(self):
        """This function checks if the object has rating field"""
        field_label = Recipe._meta.get_field("rating").verbose_name
        self.assertEqual(field_label, "rating")

    def test_recipe_rating_number(self):
        """This function checks if the object's rating is integer number"""
        recipe = Recipe.objects.get(id=1)
        field_object = Recipe._meta.get_field("rating")
        self.assertIsInstance(field_object, IntegerField)

    def test_recipe_rating_value(self):
        """This function checks if the object's rating is more then 1 and less then 10"""
        recipe = Recipe.objects.get(id=1)
        field_object = Recipe._meta.get_field("rating")
        self.assertLessEqual(field_object.value_from_object(recipe), 10)
        self.assertGreaterEqual(field_object.value_from_object(recipe), 1)

    def test_recipe_prep_time_label(self):
        """This function checks if the object has prep_time field"""
        field_label = Recipe._meta.get_field("prep_time").verbose_name
        self.assertEqual(field_label, "prep time")

    def test_reicpe_prep_time_number(self):
        """This function checks if the object's prep_time is integer number"""
        recipe = Recipe.objects.get(id=1)
        field_object = Recipe._meta.get_field("prep_time")
        self.assertIsInstance(field_object, IntegerField)

    def test_recipe_prep_time_value(self):
        """This function checks if the object's rating is more then 1"""
        recipe = Recipe.objects.get(id=1)
        field_object = Recipe._meta.get_field("prep_time")
        time = field_object.value_from_object(recipe)
        self.assertGreaterEqual(time, 1)

    def test_recipe_notes_label(self):
        """This function checks if the object has notes field"""
        field_label = Recipe._meta.get_field("notes").verbose_name
        self.assertEqual(field_label, "notes")

    def test_recipe_notes_length(self):
        """This function checks object's notes max length"""
        recipe = Recipe.objects.get(id=1)
        field_object = Recipe._meta.get_field("notes")
        content = field_object.value_from_object(recipe)
        self.assertLessEqual(len(content), 256)

    def test_recipe_notes_max_length(self):
        """This function checks object's notes max length"""
        recipe = Recipe.objects.get(id=1)
        max_length = Recipe._meta.get_field("notes").max_length
        self.assertEqual(max_length, 256)

    def test_recipe_types_label(self):
        """This function checks if the object has types field"""
        field_label = Recipe._meta.get_field("types").verbose_name
        self.assertEqual(field_label, "types")

    def test_recipe_types_length(self):
        """This function checks object's types max length"""
        recipe = Recipe.objects.get(id=1)
        field_object = Recipe._meta.get_field("types")
        content = field_object.value_from_object(recipe)
        self.assertLessEqual(len(content), 256)

    def test_recipe_types_max_length(self):
        """This function checks object's types max length"""
        recipe = Recipe.objects.get(id=1)
        max_length = Recipe._meta.get_field("types").max_length
        self.assertEqual(max_length, 256)
