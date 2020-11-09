from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class recipe(models.Model):
    id = models.AutoField(primary_key=True)

    title = models.CharField(max_length = 250)

    instructions = models.TextField()

    ingredients = models.ManyToManyField(ingredient)

    image = models.ImageField(upload_to='meshi')

    ease_of_prep = models.IntegerField(validators=[MaxValueValidator(10),MinValueValidator(1)])

    rating = models.IntegerField(validators=[MaxValueValidator(10),MinValueValidator(1)])

    prep_time_min = models.IntegerField(validators=[MinValueValidator(1)])

    notes = models.CharField(max_length = 250)

    types = models.CharField(max_length = 250)

class ingredient (models.Model):
    name = models.CharField(max_length=200)
    quantity =  models.IntegerField()
