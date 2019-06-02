#!/usr/bin/env python
"""
The complete code of Ch. 5, Recipe 7 -- 
Enumerating values the official way
"""

from collections import namedtuple
from enum import Enum, IntEnum, auto

class NumbersByName(Enum):
    zero = 0
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nine = 9

    @classmethod
    def values(cls):
        return [i.value for i in cls]

class NumbersByName2(Enum):
    zero = auto()
    one = auto()
    two = auto()
    three = auto()
    four = auto()
    five = auto()
    six = auto()
    seven = auto()
    eight = auto()
    nine = auto()

def IsArabicNumeral(value):
    return value in NumbersByName.values()

NumbersByNameTuple = namedtuple('NumbersByName', 
    [
        'zero', 'one', 'two', 'three', 'four', 'five', 
        'six', 'seven', 'eight', 'nine'
    ]
)(
    zero = 0,
    one = 1,
    two = 2,
    three = 3,
    four = 4,
    five = 5,
    six = 6,
    seven = 7,
    eight = 8,
    nine = 9,
)


if __name__ == '__main__':
    print(NumbersByName)
    # - Members are accessible by name
    print('NumbersByName.three .... %s' % NumbersByName.three)
    print('NumbersByName.one ...... %s' % NumbersByName.one)
    print('NumbersByName.four ..... %s' % NumbersByName.four)
    # - only members that were defined are available
    try:
        print(NumbersByName.thirteen)
    except Exception as error:
        print('%s: %s' % (error.__class__.__name__, error))
    # - Members' *values* are accessible by name
    print('NumbersByName.three .... %s' % NumbersByName.three.value)
    print('NumbersByName.one ...... %s' % NumbersByName.one.value)
    print('NumbersByName.four ..... %s' % NumbersByName.four.value)

    # - Members' *values* are accessible by name
    print('NumbersByName2.three ... %s' % NumbersByName2.three.value)
    print('NumbersByName2.one ..... %s' % NumbersByName2.one.value)
    print('NumbersByName2.four .... %s' % NumbersByName2.four.value)

    print('NumbersByName.__members__:')
    print(NumbersByName.__members__)
    print()

    print('Listing the members of NumbersByName:')
    print([i for i in NumbersByName])
    print()

    print('Listing the *values* of NumbersByName:')
    print([i.value for i in NumbersByName])
    print()

    print('Calling IsArabicNumeral(8):')
    print(IsArabicNumeral(8))
    print()

    print('NumbersByNameTuple:')
    print(NumbersByNameTuple)
    try:
        print(NumbersByNameTuple.thirteen)
    except Exception as error:
        print('%s: %s' % (error.__class__.__name__, error))
    try:
        NumbersByNameTuple.six = 'six'
    except Exception as error:
        print('%s: %s' % (error.__class__.__name__, error))
    print(
        'NumbersByNameTuple.three .... %s' % NumbersByNameTuple.three
    )
    print(
        'NumbersByNameTuple.one ...... %s' % NumbersByNameTuple.one
    )
    print(
        'NumbersByNameTuple.four ..... %s' % NumbersByNameTuple.four
    )
    print(
        '8 in NumbersByNameTuple: %s' % (8 in NumbersByNameTuple)
    )
