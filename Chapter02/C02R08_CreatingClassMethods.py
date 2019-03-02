#!/usr/bin/env python
"""
The complete code of Ch. 2, Recipe 8 -- Creating class methods
"""

class WithClassMethod:
    # - Define a class attribute that the class-method can use
    class_attribute = 'Spam'

    # - Define a class-method
    @classmethod
    def example(cls):
        print(
            '%s.example called on %s: %s' % 
            (cls.__name__, cls, cls.class_attribute)
        )

if __name__ == '__main__':
    # - Calling the class-method on the class it originated in
    WithClassMethod.example()

    # - Creating an instance
    wcm_instance = WithClassMethod()
    # - Calling the class-method from an instance is allowed, 
    #   but it acquires the class from the instance, keeping 
    #   the class-reference instead of using the instance:
    wcm_instance.example()

    # - Class-methods are inherited
    class InheritsClassMethod(WithClassMethod):
        class_attribute = 'Eggs'
    # - Since InheritsClassMethod.class_attribute is different 
    #   from WithClassMethod.class_attribute, we get a different 
    #   result -- the class-method references the class it's 
    #   being called against, and uses that value...
    InheritsClassMethod.example()
    # - Instance behavior is the same...
    icm_instance = InheritsClassMethod()
    icm_instance.example()
