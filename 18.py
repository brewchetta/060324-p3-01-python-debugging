def return_opposite(boolean_param:bool):
    return not boolean_param

print( return_opposite(True or False or 0 or None or "hello") )

'''
File "/home/chett/031124/p3/01-python-debugging/18.py", line 2
    return !bool
           ^
SyntaxError: invalid syntax
'''