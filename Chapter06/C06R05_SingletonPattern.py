#!/usr/bin/env python
"""
The complete code of Ch. 6, Recipe 6 -- 
Controlling how many instances can be created 
with the Singleton pattern
"""

from collections import namedtuple

# - The reference implementation, from 
#   www.python.org/download/releases/2.2/descrintro/#__new__

class Singleton(object):
    """
The original Singleton implementation mentioned in official 
Python documentation
    """
    # - Overriding __new__ to take control of how instances 
    #   are created
    def __new__(cls, *args, **kwds):
        # - Looking for a previously-created instance
        it = cls.__dict__.get('__it__')
        if it is not None:
            # - If it exists, then return it
            return it
        # - Otherwise, create, initialize, save, and return 
        #   a new instance
        cls.__it__ = it = object.__new__(cls)
        it.init(*args, **kwds)
        return it
    # - Provide a method to initialize the singleton instance
    def init(self, *args, **kwds):
        pass

# - Creating a class that uses the reference implementation of 
#   Singleton
class Example(Singleton):
    def init(self, name=None):
        self.name = name

# - Creating a few instances of Example to show what it does
example1 = Example('First Example')
print('example1 ........... %s' % example1)
print('+- example1.name ... %s' % example1.name)
example2 = Example('Second Example')
print('example2 ........... %s' % example2)
print('+- example2.name ... %s' % example2.name)
print('example1 ........... %s' % example1)
print('+- example1.name ... %s' % example1.name)
# - Changing the value of name on any instance-reference changes 
#   it for all instance-references, because they are the same 
#   object:
print('Changing example1.name:')
example1.name = 'Changed Example name'
print('+- example1.name ... %s' % example1.name)
print('+- example2.name ... %s' % example2.name)

import abc

# - A variant of the reference-implementation approach that 
#   leverages the abc module to make the init method abstract
class Singleton(metaclass=abc.ABCMeta):
    # - Unchanged from original/"reference" implementation -- 
    #   Overriding __new__ to take control of how instances 
    #   are created
    def __new__(cls, *args, **kwds):
        # - Looking for a previously-created instance
        it = cls.__dict__.get('__it__')
        if it is not None:
            # - If it exists, then return it
            return it
        # - Otherwise, create, initialize, save, and return 
        #   a new instance
        cls.__it__ = it = object.__new__(cls)
        it.init(*args, **kwds)
        return it

    # - Require a method to initialize the singleton instance
    @abc.abstractmethod
    def init(self, *args, **kwds):
        pass

# - Creating a class that uses the ABC implementation, but that 
#   doesn't define the required init method
try:
    class BadExample(Singleton):
        pass
    bad_example = BadExample('bad example')
except TypeError as error:
    print('Expected %s: %s' % (error.__class__.__name__, error))

# - Creating a class that uses the ABC implementation of Singleton
class Example(Singleton):
    def init(self, name=None):
        self.name = name

# - Creating a few instances of Example to show how it behaves
example1 = Example('First Example')
print('example1 ........... %s' % example1)
print('+- example1.name ... %s' % example1.name)
example2 = Example('Second Example')
print('example2 ........... %s' % example2)
print('+- example2.name ... %s' % example2.name)
print('example1 ........... %s' % example1)
print('+- example1.name ... %s' % example1.name)
example3 = Example('Third Example')
print('example3 ........... %s' % example3)
print('+- example3.name ... %s' % example3.name)
print('example2 ........... %s' % example2)
print('+- example2.name ... %s' % example2.name)
print('example1 ........... %s' % example1)
print('+- example1.name ... %s' % example1.name)
# - Changing the value of name on any instance-reference changes 
#   it for all instance-references, because they are the same 
#   object:
example1.name = 'Changed Example name'
print('+- example1.name ... %s' % example1.name)
print('+- example2.name ... %s' % example2.name)
print('+- example3.name ... %s' % example3.name)

