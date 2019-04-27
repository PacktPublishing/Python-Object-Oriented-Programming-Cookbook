#!/usr/bin/env python
"""
The complete code of Ch. 4, Recipe 7 -- 
Extending built-in types: Enforcing member-type on collections
"""

class TypedList(list):
    """
Provides a list-based sequence that only allows certain 
member-types
    """

    # - Keep track of allowed member-types as a read-only property
    @property
    def member_types(self):
        try:
            return self._member_types
        except AttributeError:
            return tuple()

    def __init__(self, values, **kwargs):
        # - Make sure that member_types is a sequence of values
        if type(values) not in (list, tuple):
            raise TypeError(
                '%s expects a list or tuple of values, but '
                'was passed "%s" (%s)' % 
                (
                    self.__class__.__name__, str(values), 
                    type(values).__name__
                )
            )
        member_types = kwargs.get('member_types')
        if not member_types:
            raise ValueError(
                '%s expects a list or tuple of allowed '
                'types to be specified as a member_types '
                'keyword argument, but none were supplied' % 
                (
                    self.__class__.__name__, str(values), 
                    type(values).__name__
                )
            )
        bad_types = [v for v in member_types if type(v) != type]
        if bad_types:
            raise ValueError(
                '%s expects a list or tuple of allowed '
                'types to be specified as a member_types '
                'keyword argument, but was passed "%s" (%s), '
                'which contained invalid value-types (%s)' % 
                (
                    self.__class__.__name__, str(values), 
                    type(values).__name__, ', '.join(bad_types)
                )
            )
        # - Set the allowed member-types
        self._member_types = tuple(member_types)
        # - Check the provided values
        for member in values:
            self._type_check(member)
        # - If everything checks as valid, then call the parent 
        #   object-initializer (list.__init__)
        list.__init__(self, values)

    # - Create a type-checking helper-method
    def _type_check(self, member):
        # - Using isinstance instead of a straight type-
        #   comparison, so that extensions of types will be 
        #   accepted too
        if not isinstance(member, self.member_types):
            raise TypeError(
                'This instance of %s only accepts %s values: '
                '%s (%s) is not allowed' % 
                (
                    self.__class__.__name__, 
                    '|'.join(
                        [t.__name__ for t in self.member_types]
                    ), str(member), type(member).__name__
                )
            )

    # - Wrap all of the list methods that involve adding a member 
    #   with type-checking
    def __add__(self, other):
        # - Called when <list> + <list2> is executed
        for member in other:
            self._type_check(member)
        # - list.__add__ returns a new list with the new members
        return TypedList(
            list.__add__(self, other), 
            member_types=self.member_types
        )

    def __iadd__(self, other):
        # - Called when <list> += <list2> is executed
        for member in other:
            self._type_check(member)
        # - list.__iadd__ returns the instance after it's 
        #   been modified
        return list.__iadd__(self, other)

    def __mul__(self, other):
        # - Called when <list> * <int> is executed
        # - list.__mul__ returns a new list with the new members
        return TypedList(
            list.__mul__(self, other), 
            member_types=self.member_types
        )

    def append(self, member):
        self._type_check(member)
        return list.append(self, member)

    def extend(self, other):
        for member in other:
            self._type_check(member)
        return list.extend(self, other)

    def insert(self, index, member):
        self._type_check(member)
        return list.insert(self, index, member)

number_list = TypedList([1,], member_types=(float,int))
print(number_list)
print(type(number_list))

try:
    number_list = TypedList(['not-a-number',], member_types=(float,int))
    print(number_list)
    print(type(number_list))
except Exception as error:
    print('%s: %s' % (error.__class__.__name__, error))

number_list = TypedList([1,], member_types=(float,int))
number_list = number_list + [3.14]
print(number_list)
print(type(number_list))

number_list = number_list * 2
print(number_list)
print(type(number_list))

# ~ number_list = TypedList([1,], member_types=(float,int))
# ~ number_list += [2.3]
# ~ print(number_list)
# ~ print(type(number_list))

# ~ number_list.append(4.5)
# ~ print(number_list)
# ~ print(type(number_list))

number_list = TypedList([1,], member_types=(float,int))
number_list *= 2
print(number_list)
print(type(number_list))

number_list = TypedList([1,], member_types=(float,int))
# ~ number_list.insert(0, 0)
# ~ print(number_list)
# ~ print(type(number_list))

number_list = TypedList([1,], member_types=(float,int))
# ~ number_list.extend([7,8.9])
# ~ print(number_list)
# ~ print(type(number_list))

