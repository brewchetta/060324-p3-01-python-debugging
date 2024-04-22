cats = ["Octavia", "Ursula"]

def cats():
    for cats in cats:
        cats.append(f"Meow my name is {cats}")
    return cats

print( cats() )

'''
File "/home/chett/031124/p3/01-python-debugging/06.py", line 4, in cats
    for cats in cats:
UnboundLocalError: local variable 'cats' referenced before assignment
'''