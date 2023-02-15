import inspect
import requests

print(inspect.ismodule(requests))
print(inspect.isclass(requests))
print(inspect.isfunction(requests))

print(inspect.getmodule(requests.get))
print(inspect.getmodule(list))

class Human:
    def __init__(self, age, height=170, name='John'):
        self.age = age
        self.height = height
        self.name = name
        self.secondame = 'Wick'

sig = inspect.signature(Human)
for parameter in sig.parameters.values():
    print(parameter.name, parameter.default)

import sys

print(sys.executable)
print(sys.version)

print(sys.platform)
print(sys.argv)

for module_name, module_path in sys.modules.items():
    print(f"{module_name} - {module_path}")

print("""
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
""")


for _ in dir(__builins__)
    print(_)






