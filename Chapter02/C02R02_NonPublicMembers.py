#!/usr/bin/env python
"""
The complete code of Ch. 2, Recipe 2 -- Restricting member access
"""

class BasicClass:
    """Document the class as needed"""
    # Comments are allowed in classes
    # - Object initialization
    def __init__(self, name, description):
        """Object initialization"""
        # - Initialize instance properties from arguments
        self.name = name
        self.description = description
    # - Instance method
    def summarize(self):
        """Document method"""
        if self.description:
            return '%s: %s' % (self.name, self.description)
        else:
            return self.name

    # - Private method
    def __private_method(self):
        return '__private_method called'

    # - Protected method
    def _protected_method(self):
        return '_protected_method called'

if __name__ == '__main__':
    print('#'*66)
    print('# BasicClass'.ljust(65, ' ') + '#')
    print('#'*66)
    print(BasicClass)
    # - Create an instance of the class
    my_object = BasicClass('my name', 'my description')
    print('#- BasicClass instance '.ljust(65, '-') + '#')
    print(my_object)
    # - This is allowed, but is NOT according to convention
    print(my_object._protected_method())
    # - The name-mangling of private members prevents casual 
    #   access to them:
    try:
        print(my_object.__private_method())
    except Exception as error:
        print('### %s: %s' % (error.__class__.__name__, error))
    # - But they can still be accessed. Again, this is **NOT** 
    #   according to Python conventions, so don't do this!
    print(my_object._BasicClass__private_method())
