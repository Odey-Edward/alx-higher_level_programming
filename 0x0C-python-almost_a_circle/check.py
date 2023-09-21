import inspect
from models.rectangle import Rectangle

fuc = inspect.getmembers(Rectangle, inspect.isfunction)

for v in fuc:
    print(v[0].__doc__)
