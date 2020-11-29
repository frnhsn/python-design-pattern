"""
Ensure a class only has one instance, and provide a global point of
access to it.
"""

class Singleton(type):
    """
    Define an Instance operation that lets clients access its unique
    instance.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class SingletonClass(metaclass=Singleton):
    pass

class SecondSingletonClass(metaclass=Singleton):
    pass

o1 = SingletonClass()
o2 = SingletonClass()
o3 = SecondSingletonClass()

print(id(o1))
print(id(o2))
print(id(o3))
    
