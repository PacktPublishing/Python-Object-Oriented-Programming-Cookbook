#!/usr/bin/env python
"""
The complete code of Ch. 2, Recipe 5 -- Defining properties using property as a function
"""

class BasicClass:
    """Document the class as needed"""

    # - Object initialization
    def __init__(self, name, description):
        """Object initialization"""
        # - Initialize instance properties from arguments
        self.name = name
        self.description = description

    # Defining description as a property using the 
    # function approach

    # - Define a getter-method
    def _get_description(self):
        try:
            return self._description
        except AttributeError:
            return None

    # - Define a setter-method
    def _set_description(self, value):
        if type(value) != str:
            raise TypeError('description expects a string value')
        self._description = value

    # - Define a deleter-method
    def _del_description(self):
        try:
            del self._description
        except AttributeError:
            pass

    # - Assemble them into a property
    description = property(
        _get_description, _set_description, _del_description, 
        'Gets, sets or deletes the description associated with the instance'
    )

# - Show the documentation of the property
print('1) %s' % BasicClass.description.__doc__.strip())
# - Create an instance.
my_object = BasicClass('name', 'description')
# - Show the original value
print('2) %s' % my_object.description)
# - Alter the value, and show it again
my_object.description='A new description'
print('3) %s' % my_object.description)
# - Show that the type-checking works
try:
    my_object.description = 123.456
except Exception as error:
    print('4) %s: %s' % (error.__class__.__name__, error))

