from faker import Faker

fake = Faker()

person = {
    'name': fake.name(),
    'address': fake.address(),
    'email': fake.email()
}

print( person )

'''
Traceback (most recent call last):
  File "10.py", line 9, in <module>
    'phone': fake.phone()
  File "/home/chett/Flatiron/060324/p3/01-python-debugging/.venv/lib/python3.8/site-packages/faker/proxy.py", line 130, in __getattr__
    return getattr(self._factories[0], attr)
AttributeError: 'Generator' object has no attribute 'phone'
'''