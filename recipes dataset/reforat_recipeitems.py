import json

out_file = {}

with open("recipes dataset/20170107-061401-recipeitems.json", "r") as json_file:

    index = 1
    for recipe in json_file:
        out_file[index] = json.loads(recipe)
        index += 1

with open("recipes dataset/recipe_items.json", "w") as outfile:
    json.dump(out_file, outfile)
