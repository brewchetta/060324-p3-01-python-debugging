raccoon_dictionary = { 'name': 'Bob', 'age': 21 }

def get_raccoon_name(raccoon:dict):
    return raccoon.name

print( get_raccoon_name() )

'''
File "/home/chett/031124/p3/01-python-debugging/07.py", line 6, in <module>
    print( get_raccoon_name() )
TypeError: get_raccoon_name() missing 1 required positional argument: 'raccoon'
'''