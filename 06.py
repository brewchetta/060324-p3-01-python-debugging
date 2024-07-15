cat_list = ["Octavia", "Ursula"]

def cat_names(cat_list):
    # global cat_list
    result = []
    for cat in cat_list:
        result.append(f"Meow my name is {cat}")
    return result

print( cat_names(cat_list) )

'''
File "/home/chett/031124/p3/01-python-debugging/06.py", line 4, in cats
    for cats in cats:
UnboundLocalError: local variable 'cats' referenced before assignment
'''