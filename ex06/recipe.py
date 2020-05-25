cookbook = {
    'sandwich': {
        'ingredients':
        ['ham', 'bread', 'cheese', 'tomatoes'],
        'meal': 'lunch',
        'prep_time': 10
    },
    'cake': {
        'ingredients':
        ['flour', 'sugar', 'egg'],
        'meal': 'dessert',
        'prep_time': 60
    },
    'salad': {
        'ingredients':
        ['avocado', 'arugula', 'tomatoes', 'spinach'],
        'meal': 'lunch',
        'prep_time': 15
    }
}


def print_recipe(recipeName):
    print("Recipe for {}".format(recipeName))
    print("Ingredients list: {}".format(cookbook[recipeName]['ingredients']))
    print("To be eaten for {}".format(cookbook[recipeName]['meal']))
    print("Takes {} min to cook".format(cookbook[recipeName]['prep_time']))


def del_recipe(recipeName):
    if recipeName in cookbook:
        del cookbook[recipeName]
        print("The {} recipe is deleted from the cookbook".format(recipeName))


def add_recipe(name, ingredients, mtype, time):
    cookbook[name] = {
        'ingredients': ingredients,
        'meal': mtype,
        'prep_time': time
    }


def print_all():
    for i in cookbook:
        print("")
        print_recipe(i)


def print_allNames():
    for i in cookbook:
        print(i)


def menuadd():
    name = input("Please type the name of the recipe to add\n")
    meal = input("What type of meal is it ?\n")
    prep_time = input("How long does it take to make (in minuts)\n")
    ing = input("List ingredients separated by a coma\n")
    ingredients = ing.split(',')
    add_recipe(name, ingredients, meal, prep_time)
    print("Recipe added")
    menu()


def menudel():
    name = input("Please type the name of the recipe to delete\n")
    del_recipe(name)
    menu()


def menuprint():
    try:
        name = input("Please type the name of the recipe to print\n")
        print_recipe(name)
    except KeyError:
        print("This recipe isn't in the cookbook yet")
    menu()


def menu():
    print("\nPlease select an option by tiping the right number")
    print("1. Add a recipe\n2. Delete a recipe")
    print("3. Print a recipe\n4. Print the cookbook")
    print("5. Quit")
    choice = input("\n")
    if choice == '1':
        menuadd()
    elif choice == '2':
        menudel()
    elif choice == '3':
        menuprint()
    elif choice == '4':
        print_all()
        menu()
    elif choice == '5':
        quit()
    else:
        menu()


menu()

# add_recipe("carbonara", ["pate", "lard", "oeuf", "parmesant"], "lunch", 60)
# print_all()

# Recipe for cake:
# Ingredients list: ['flour', 'sugar', 'eggs']
# To be eaten for dessert.
# Takes 60 minutes of cooking.
