from faker import Faker

fake = Faker()

person = {
    'name': fake.name(),
    'address': fake.address(),
    'email': fake.email(),
    'phone': fake.phone()
}

print( person )

'''
File "/home/chett/031124/p3/01-python-debugging/10.py", line 1, in <module>
    from faker import Faker
ModuleNotFoundError: No module named 'faker'
'''