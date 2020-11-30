from django.contrib import admin
from .models import Recipe
from .models import Ingredient

admin.site.register(Ingredient)

class RecipeAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "title",
        "ease_of_prep",
        "rating",
        "prep_time", 
    )

    search_fields = (
        "title",
        "rating",
    )

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Recipe, RecipeAdmin)
