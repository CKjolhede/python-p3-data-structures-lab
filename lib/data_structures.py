import ipdb

spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [ food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [ food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(food["name"] + " (" + food["cuisine"] + ") | Heat Level: " + "🌶" * food["heat_level"])
    return


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    foods = [food for food in spicy_foods if food["cuisine"] == cuisine]
    return foods[0]

def print_spiciest_foods(spicy_foods):
    foods = [food for food in spicy_foods if food['heat_level'] > 5]
    for food in foods:
        print(food["name"] + " (" + food["cuisine"] + ") | Heat Level: " + "🌶" * food["heat_level"])
    return

def get_average_heat_level(spicy_foods):
    #levels = []
    #for food in spicy_foods:
    #    levels.append[food["heat_level"]]
    levels = [food["heat_level"] for food in spicy_foods]
    ave = sum(levels)/len(levels)
    print(ave)
    return ave

def create_spicy_food(spicy_foods, spicy_food):
    foods = [food for food in spicy_foods]
    foods.append(spicy_food)
    return foods

#ipdb.set_trace()