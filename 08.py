street_fighters = {
    "name": "Ryu",
    "special_move": "Hadouken"
} # dictionary

def print_street_fighters(fighters:list):
    for fighter in fighters:
        print(fighter)
        print(f"{fighter['name']}'s special move is {fighter['special_move']}")

print_street_fighters( street_fighters )

'''
File "/home/chett/031124/p3/01-python-debugging/08.py", line 8, in print_street_fighters
    print(f"{fighter['name']}'s special move is {fighter['special_move']}")
TypeError: string indices must be integers
'''