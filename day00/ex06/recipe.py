# Part 1: Nested Dictionaries

# Create a dictionary called cookbook.
# cookbook will contain 3 recipes:
#   • Sandwich
#       ingredients are: ham, bread, cheese and tomatoes
#       meal is: lunch
#       prep_time is: 10 minutes
#
#   • The Cake
#       ingredients are: flour, sugar and eggs
#       meal is: dessert
#       prep_time is: 60 minutes
#
#   • The Salad
#       ingredients are: avocado, arugula, tomatoes and spinach
#       meal is: lunch
#       prep_time is: 15 minutes

cookbook = {
    "Sandwich": {
        "ingredients": ["ham", "bread", "cheese", "tomatoes"],
        "meal": "lunch",
        "prep_time": 0,
    },
    "Cake": {
        "ingredients": ["flour", "sugar", "eggs"],
        "meal": "dessert",
        "prep_time": 60,
    },
    "Salad": {
        "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
        "meal": "lunch",
        "prep_time": 15,
    },
}
# -------------------------------------------------------------------


### Part 2: A series of Helpful Functions

# Create a series of useful functions to handle your cookbook:


#   1. A function that print all recipe names.
def print_recipes():
    print('-----------')
    print('ALL RECIPES')
    print('-----------')
    for recipe in cookbook: print(recipe)
    print('-----------')


#   2. A function that takes a recipe name and print its details.
def recipe_details(recipe_name: str):
    print('The meal is {:s}'.format(recipe_name))

    if recipe_name in cookbook.keys():
        print('It\'s ingredients are {:s}.'.format(', '.join(cookbook[recipe_name]['ingredients'])))
        print('It is a {:s} meal.'.format(cookbook[recipe_name]['meal']))
        print('It takes {:d} of preparation.'.format(cookbook[recipe_name]['prep_time']))
    else:
        print('This meal does not exist in the Cookbook!')


#   3. A function that takes a recipe name and delete it.
def remove_recipe(recipe_name: str):
    if recipe_name in cookbook.keys():
        cookbook.pop(recipe_name)
    else:
        print('This meal does not exist in the Cookbook!')
    pass


#   4. A function that add a recipe from user input. You will need a name, a list of
#      ingredient, a meal type and a preparation time
def add_recipe():

    recipe_name = input('Enter a recipe name:\n').strip()
    if len(recipe_name) == 0 or recipe_name in cookbook.keys():
        print('This recipe is invalid/exists!')
        return

    recipe_ingr = input('Enter ingredients seperated by comma(,) :\n')
    recipe_ingr = recipe_ingr.split(',')
    recipe_ingr = [ingr.strip() for ingr in recipe_ingr]
    if len(recipe_ingr) == 0 or all([ingr == '' for ingr in recipe_ingr]):
        print('Invalid ingredients!')
        return

    recipe_meal = input('Enter meal type:\n').strip()
    if len(recipe_meal) == 0:
        print('Please specify a meal next time!')
        return
    
    recipe_time = int(input('Enter time mintues for preparation:\n').strip())
    if recipe_time <= 0:
        print('Please enter a positive number next time!')

    # cookbook[recipe_name] = { 'ingredients': recipe_ingr, 'meal': recipe_meal, 'prep_time': recipe_time } # 1
    cookbook.update( { recipe_name: { 'ingredients': recipe_ingr, 'meal': recipe_meal, 'prep_time': recipe_time } } ) # 2

    pass


if __name__ == '__main__':
    # print_recipes()
    # print()

    # recipe_details('Salad')
    # print()
    # recipe_details('Sandwich')
    # print()
    # recipe_details('Cake')
    # print()
    # recipe_details('CakeSalad')

    # print()
    # remove_recipe('CakeSalad')
    # print()
    # remove_recipe('Salad')
    # print_recipes()

    add_recipe()
    print()
    # print_recipes()
    print(cookbook.items())

    pass