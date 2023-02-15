import requests
def first_function():
    pass

class Human:
    pass

rq = requests
nick = Human
first_f = first_function

print(requests.__name__)
print(rq.__name__)
print(Human.__name__)
print(nick.__name__)
print(first_f.__name__)
print(first_function.__name__)
'''
intro_list = []
for method in dir(intro_list):
    print(method)

print(__name__)
'''

for method in dir():
    print(method)

data = 'strings'
print(hasattr(data, "reverse"))
print(hasattr(data, 'index'))

print(getattr(data, "startswith"))
print(getattr(data, "startswith", None))
print(getattr(data, "reverse", None))



