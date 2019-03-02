#!/usr/bin/env python
"""
The complete code of Ch. 2, Recipe 6 -- Passing object-state during construction
"""

class Person:
    """A *very* basic representation of a person"""

    def __init__(self, 
        # - Required Person arguments
        given_name:str, family_name:str, 
        # - Optional Person arguments
        birth_date:(str,None)=None, email_address:(str,None)=None
    ):
        """Object initialization"""
        self.given_name = given_name
        self.family_name = family_name
        self.birth_date = birth_date
        self.email_address = email_address

    def __str__(self):
        """Returns a string representation of the object"""
        return (
            '<%s [%s] given_name=%s family_name=%s>' % 
            (
                self.__class__.__name__, hex(id(self)), 
                self.given_name, self.family_name, 
            )
        )

if __name__ == '__main__':
    author = Person('Brian', 'Allbee')
    print(author)

    alice = Person(
        'Alice', 'Exeter', None, 'aexeter@some-company.com'
    )
    print(alice)
    print(alice.birth_date)
    print(alice.email_address)

    bob = Person('Robert', 'Jones', '1959-03-21')
    print(bob)
    print(bob.birth_date)
    print(bob.email_address)

