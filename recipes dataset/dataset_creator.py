import json


def calc_minutes(str_time):
    og_str_time = str_time
    print(og_str_time)
    if str_time is None or not str_time or str_time == "PT" or "PT" not in str_time:
        return ""
    str_time = str_time[2:]
    if "S" in str_time and "M" in str_time:
        return int(str_time.split("M")[0]) + 1
    if "S" in str_time:
        return 1
    if "H" not in str_time:
        return int(str_time[:-1])
    if "M" not in str_time:
        return int(str_time[:-1]) * 60
    if "M" in str_time and "H" in str_time:
        str_time = str_time.split("H")
        h = int(str_time[0])
        m = int(str_time[1][:-1])
        return h * 60 + m
    raise Exception("Unexpected time pattern {}".format(og_str_time))


def calc_yield(str_yield):
    print(str_yield)
    r = ""
    if str_yield is None or str_yield == "Serves":
        return ""
    if "Serves" in str_yield:
        r = str_yield.split()[1][:-1]
    if "servings" in str_yield:
        r = str_yield.split()[0]
    try:
        r = int(r)
    except ValueError:
        print("Unexpected yield pattern {}".format(str_yield))
    return r


recipes_dataset = {}


with open("recipes dataset/recipe_items.json", "r") as json_file:
    recipes = json.load(json_file)
    for idx in recipes:
        recipe = recipes[idx]
        print(idx)
        try:
            recipes_dataset[idx] = {
                "title": recipe["name"],
                "type": "",
                "ingredients": recipe["ingredients"].split("\n"),
                "instructions": [],
                "image": recipe.get("image", ""),
                "rating": "",
                "ease_of_prep": "",
                "prep_time": calc_minutes(recipe.get("prepTime", None)),
                "cook_time": calc_minutes(recipe.get("cookTime", None)),
                "yield": calc_yield(recipe.get("recipeYield", None)),
                "notes": recipe.get("description", ""),
            }
        except EnvironmentError:
            print("Skipping index {}".format(idx))

with open("recipes dataset/recipes_dataset.json", "w") as outfile:
    json.dump(recipes_dataset, outfile)
