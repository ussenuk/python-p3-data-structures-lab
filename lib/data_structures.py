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
    food_name_list=[]
    for food_data in spicy_foods:
        food_names = food_data['name']
        food_name_list.append(food_names)
    return food_name_list

def get_spiciest_foods(spicy_foods):
    spiciest_food_list=[]
    for food_data in spicy_foods:
        if food_data['heat_level'] > 5:
            spiciest_food_list.append(food_data)
    return spiciest_food_list

def print_spicy_foods(spicy_foods):
    for food_data in spicy_foods:
        print (food_data['name'],'('+food_data['cuisine']+')', '|', 'Heat Level:',food_data['heat_level'] *'🌶')

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food_data in spicy_foods:
        if food_data['cuisine'] == cuisine:
            return food_data

def print_spiciest_foods(spicy_foods):
    for food_data in spicy_foods:
        if food_data['heat_level'] > 5:
            print (food_data['name'],'('+food_data['cuisine']+')', '|', 'Heat Level:', food_data['heat_level'] *'🌶')


def get_average_heat_level(spicy_foods):
        total = 0
        for food_data in spicy_foods:
            total += food_data['heat_level']
        print (total // len(food_data))

def create_spicy_food(spicy_foods, spicy_food):
    pass
