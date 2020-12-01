from django.contrib import admin
from recipes.models import Recipe
from recipes.models import Ingredient


class IngredientAdmin(admin.ModelAdmin):

    list_display = ("id", "name")

    search_fields = ("name",)

    filter_horizontal = ()
    list_filter = ()


class RecipeAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "title",
        "instructions",
        "get_ingredients",
        "image",
        "ease_of_prep",
        "rating",
        "prep_time",
        "notes",
        "types",
    )

    search_fields = (
        "title",
        "instructions",
        "ingredients__name",
        "ease_of_prep",
        "rating",
        "prep_time",
        "types",
    )

    filter_horizontal = ("ingredients",)
    list_filter = (
        "ease_of_prep",
        "rating",
        "prep_time",
        "types",
        "ingredients__name",
    )

    def get_ingredients(self, recipe):
        return "\n".join([ingredient.name for ingredient in recipe.ingredients.all()])


admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
