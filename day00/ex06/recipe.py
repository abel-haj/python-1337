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
    "sandwich": {
        "ingredients": ["ham", "bread", "cheese", "tomatoes"],
        "meal": "lunch",
        "prep_time": 0,
    },
    "cake": {
        "ingredients": ["flour", "sugar", "eggs"],
        "meal": "dessert",
        "prep_time": 60,
    },
    "salad": {
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
    print('-----------\n')


#   2. A function that takes a recipe name and print its details.
def print_recipe(recipe_name: str):
    recipe_name = recipe_name.lower()
    print('Recipe for {:s}'.format(recipe_name))

    if recipe_name in cookbook.keys():
        print('\tIngredients list: [{:s}]'.format(', '.join(cookbook[recipe_name]['ingredients'])))
        print('\tTo be eaten for {:s}.'.format(cookbook[recipe_name]['meal']))
        print('\tTakes {:d} minutes of cooking.'.format(cookbook[recipe_name]['prep_time']))
    else:
        print('This meal does not exist in the Cookbook!')
    print('')


#   3. A function that takes a recipe name and delete it.
def remove_recipe(recipe_name: str):
    recipe_name = recipe_name.lower()
    if recipe_name in cookbook.keys():
        cookbook.pop(recipe_name)
        print('{:s} recipe deleted!'.format(recipe_name))
    else:
        print('This meal does not exist in the Cookbook!')
    print('')


#   4. A function that add a recipe from user input. You will need a name, a list of
#      ingredient, a meal type and a preparation time
def add_recipe():

    recipe_name = input('Enter a recipe name:\n').strip().lower()
    if len(recipe_name) == 0 or recipe_name in cookbook.keys():
        print('This recipe is invalid/exists!')
        return

    recipe_ingr = input('Enter ingredients seperated by comma(,) :\n')
    recipe_ingr = recipe_ingr.split(',')
    recipe_ingr = [ingr.strip() for ingr in recipe_ingr]
    if len(recipe_ingr) == 0 or all([ingr == '' for ingr in recipe_ingr]):
        print('Invalid ingredients!\n')
        return

    recipe_meal = input('Enter meal type:\n').strip()
    if len(recipe_meal) == 0:
        print('Please specify a meal next time!\n')
        return
    
    recipe_time = input('Enter time mintues for preparation:\n').strip()

    if not recipe_time.isnumeric():
        print('Please enter a number next time!\n')
        return

    recipe_time = int(recipe_time)
    if recipe_time <= 0:
        print('Please enter a positive number next time!\n')
        return

    # cookbook[recipe_name] = { 'ingredients': recipe_ingr, 'meal': recipe_meal, 'prep_time': recipe_time } # 1
    cookbook.update( { recipe_name: { 'ingredients': recipe_ingr, 'meal': recipe_meal, 'prep_time': recipe_time } } ) # 2
    print('{:s} recipe was added!\n'.format(recipe_name))


def print_prompt():
    print('List of available option:')
    print('\t1: Add a recipe')
    print('\t2: Delete a recipe')
    print('\t3: Print a recipe')
    print('\t4: Print the cookbook')
    print('\t5: Quit\n')
    pass


if __name__ == '__main__':

    print('Welcome to the Python Cookbook !')
    while 1:
        print_prompt()
        choice = input('Please select an option: ')
        if not choice.isnumeric():
            print('Not a valid number\n')
            continue
        choice = int(choice)

        match choice:
            case 1:
                add_recipe()
            case 2:
                print('Please enter a recipe name to delete it:')
                remove_recipe(input())
            case 3:
                print('Please enter a recipe name to get its details:')
                print_recipe(input())
            case 4:
                print_recipes()
            case 5:
                print('Cookbook closed. Have a nice day!')
                break

            case _:
                print('Wrong value entered! Please try again!\n')

    pass