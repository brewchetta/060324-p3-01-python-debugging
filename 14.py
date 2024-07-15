bundt_cake_ingredients = ['flour', 'baking powder', 'baking soda', 'butter', 'sugar', 'eggs', 'buttermilk', 'vanilla']

def make_cake(name:str, ingredients_list:list):

    return f"Making a {name} with these ingredients: { ', '.join(ingredients_list) }"


bundt_cake = make_cake( ingredients_list=bundt_cake_ingredients, name="Bundt Cake" )

print( bundt_cake )

'''
Traceback (most recent call last):
  File "14.py", line 8, in <module>
    bundt_cake = make_cake( bundt_cake_ingredients )
TypeError: make_cake() missing 1 required positional argument: 'ingredients_list'
'''