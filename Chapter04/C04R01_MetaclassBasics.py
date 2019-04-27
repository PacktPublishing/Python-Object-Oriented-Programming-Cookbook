#!/usr/bin/env python
"""
The complete code of Ch. 4, Recipe 1 -- 
Taking control of class creation with metaclasses
"""

print('Defining the BasicMetaclass metaclass')

class BasicMetaclass(type):
    def __new__(cls, *args, **kwargs):
        # - Print some information, so that what's happening 
        #   is visible
        print('BasicMetaclass.__new__ called:')
        # - The args passed are the name of the new class, the 
        #   base classes that the new class inherits from, and 
        #   a dict of items that includes the module, the 
        #   qualified name of the class, and a reference to 
        #   the __init__ to be called...
        print('+- *args ....... %s' % str(args))
        print('+- *kwargs ..... %s' % str(kwargs))
        # - Delegate to superclass for actual object-creation
        new_class = super().__new__(cls, *args, **kwargs)
        print('+- new_class ... %s' % new_class)
        # - Return the new class
        return new_class

print('BasicMetaclass defined')

print('Defining the UsesMeta class that uses the metaclass')

class UsesMeta(metaclass=BasicMetaclass):
    def __init__(self, arg, *args, **kwargs):
        print('UsesMeta.__init__ called:')
        print('+- *arg ........ %s' % arg)
        print('+- *args ....... %s' % str(args))
        print('+- *kwargs ..... %s' % str(kwargs))

print('UsesMeta defined')

instance = UsesMeta('argument', 'args1', 'args2', keyword='value')

print(type(instance))
