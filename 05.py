number_variable = 0

def add_to_number_variable(num:int):
    number_variable += num
    return number_variable

print( add_to_number_variable(5) )

'''
File "/home/chett/031124/p3/01-python-debugging/05.py", line 4, in add_to_number_variable
    number_variable += num
UnboundLocalError: local variable 'number_variable' referenced before assignment
'''