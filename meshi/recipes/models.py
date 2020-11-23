from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length = 256)
    instructions = models.TextField()
    ingredients = models.ManyToManyField(ingredient)
    image = models.ImageField(upload_to='meshi')
    ease_of_prep = models.IntegerField(validators=[MaxValueValidator(10),MinValueValidator(1)])
    rating = models.IntegerField(validators=[MaxValueValidator(10),MinValueValidator(1)])
    prep_time_min = models.IntegerField(validators=[MinValueValidator(1)])
    notes = models.CharField(max_length = 256)
    types = models.CharField(max_length = 256)

class Ingredient (models.Model):
    """
    Examples from our datebase:

    1 teaspoon baking soda
    1 teaspoon vanilla extract
    2 eggs, preferably at room temperature
    4 slices Bacon, Cooked And Crumbled

    so each element is a string
    """
    name = models.CharField(max_length = 128)