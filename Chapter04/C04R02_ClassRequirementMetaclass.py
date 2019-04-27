#!/usr/bin/env python
"""
The complete code of Ch. 4, Recipe 2 -- 
Enforcing class requirements with metaclass
"""

### Enforcing class-attribute requirements with a metaclass
# - This class, intended to be used as a metaclass, requires 
#   that a CLASS DEFINITION using it include some required 
#   class-attributes. This requirement is enforced DURING 
#   THE DEFINITION OF THE CLASS, rather than during instantiation 
#   of an instance of the class because it's implemented in 
#   __new__

class RequireParms(type):
    # - Define the attribute-names that are required when this 
    #   metaclass is attached to another class
    _required_attrs = (
        '_required',        # - Some required attribute
        '_also_required',   # - Another required attribute
    )

    def __new__(cls, *args, **kwargs):
        # - Delegate to superclass for actual object-creation
        new_class = super().__new__(cls, *args, **kwargs)
        # - Check for required class-attributes
        for required_attribute in \
            RequireParms._required_attrs:
            if not hasattr(new_class, required_attribute) \
                or getattr(new_class, required_attribute) == None:
                raise AttributeError(
                    '%s does not supply a non-None %s attribute' %
                    (new_class.__name__, required_attribute)
                )
        return new_class

if __name__ == '__main__':
    # - This class-definition, for example, will fail, because it 
    #   doesn't have the required class-attributes defined...
    try:
        class Oook(metaclass=RequireParms):
            # - Uncomment these to see how the tests progress
            #_required = 'Required attribute'
            #_also_required = 'Another required attribute'
            pass
    except Exception as error:
        print('%s: %s' % (error.__class__.__name__, error))

    # - This one will work, though -- It *does* define the 
    #   required class-attributes...
    class Eeek(metaclass=RequireParms):
        _required = True
        _also_required = 1

    print(
        '_required: %s; _also_required: %s' % 
        (Eeek._required, Eeek._also_required)
    )
    test_instance = Eeek()
    print(
        '_required: %s; _also_required: %s' % 
        (test_instance._required, test_instance._also_required)
    )
