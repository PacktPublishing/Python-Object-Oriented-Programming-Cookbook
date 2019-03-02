#!/usr/bin/env python
"""
The complete code of Ch. 2, Recipe 4 -- Defining properties using property as a decorator
"""

class BasicClass:
    """Document the class as needed"""

    # - Object initialization
    def __init__(self, name:str, description:str):
        """Object initialization"""
        # - Initialize instance properties from arguments
        self.name = name
        self.description = description

    # Defining name as a property
    # - Start with the getter assignment
    @property
    def name(self) -> (str,None):
        """
Gets, sets or deletes the name associated with the instance
        """
        try:
            return self._name
        except AttributeError:
            return None

    # - Assign a protected method that checks for a string 
    #   type as the setter for name
    @name.setter
    def name(self, value:str) -> None:
        """Sets the name associated with the instance"""
        if type(value) != str:
            raise TypeError('name expects a string value')
        self._name = value

    # - Assign a deleter-method
    @name.deleter
    def name(self) -> None:
        try:
            del self._name
        except AttributeError:
            pass

# - Show the documentation of the property
print('1) %s' % BasicClass.name.__doc__.strip())
# - Create an instance.
my_object = BasicClass('name', 'description')
# - Show the original value
print('2) %s' % my_object.name)
# - Alter the value, and show it again
my_object.name='A new name'
print('3) %s' % my_object.name)
# - Show that the type-checking works
try:
    my_object.name = 123.456
except Exception as error:
    print('4) %s: %s' % (error.__class__.__name__, error))

