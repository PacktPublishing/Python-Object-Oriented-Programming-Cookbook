#!/usr/bin/env python
"""
The complete code of Ch. 2, Recipe 9 -- Creating static methods
"""

class WithStaticMethod:
    def instance_method(self):
        pass
    @staticmethod
    def static_method():
        print('WithStaticMethod.static_method called')

if __name__ == '__main__':
    print(type(WithStaticMethod))
    # - All of these report that they are *functions* rather 
    #   than methods...
    print(WithStaticMethod.static_method)
    print(WithStaticMethod.instance_method)

    # - For comparison purposes, what does a normal function look 
    #   like when it's printed?
    def some_function():
        pass
    print(some_function)

    # - Creating an instance...
    wsm_instance = WithStaticMethod()
    print(wsm_instance)
    # - Still reports that it's a function
    print(wsm_instance.static_method)
    # - Since this is associated with an instance, it reports 
    #   that it's a bound method
    print(wsm_instance.instance_method)
    wsm_instance.static_method()

    # - The static method is inherited unchanged...
    class InheritsStaticMethod(WithStaticMethod):
        pass

    print(InheritsStaticMethod.static_method)
    InheritsStaticMethod.static_method()
    ism_instance = InheritsStaticMethod()
    ism_instance.static_method()
