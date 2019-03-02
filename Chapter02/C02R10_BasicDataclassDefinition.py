#!/usr/bin/env python
"""
The complete code of Ch. 2, Recipe 10 -- Simplifying class definitions: The dataclasses module
"""

from dataclasses import dataclass

@dataclass(order=True)
class Person:
    """
A *very* basic representation of a person, created as a dataclass
"""
    given_name: str
    family_name: str
    birth_date: str = None
    email_address: str = None

if __name__ == '__main__':
    # - Classes defined as dataclasses are still classes...
    print(Person)
    # - They still appear as normal "type" types
    print(type(Person))
    # - They have additional members
    print('__annotations__ ........ %s' % Person.__annotations__)
    print('__dataclass_fields__ ... %s' % Person.__dataclass_fields__)
    print('__dataclass_params__ ... %s' % Person.__dataclass_params__)
    # - And have some that have default implementations provided:
    author = Person('Brian', 'Allbee')
    print(author)
    alice = Person(
        'Alice', 'Exeter', None, 'aexeter@some-company.com'
    )
    print(alice)
    # - order=True has to be passed as an argument to the 
    #   dataclass decorator for these to work:
    print('author == alice ... %s' % (author == alice))
    print('author != alice ... %s' % (author != alice))
    print('author < alice .... %s' % (author < alice))
    print('author <= alice ... %s' % (author <= alice))
    print('author > alice .... %s' % (author > alice))
    print('author >= alice ... %s' % (author >= alice))

    author = PersonWithProperties('Brian', 'Allbee')
    print(author)
