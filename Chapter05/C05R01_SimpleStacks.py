#!/usr/bin/env python
"""
The complete code of Ch. 5, Recipe 1 -- 
Implementing a simple stack
"""

from random import randint

def print_line(
    leader:str, line:(str,None)=None, 
    indent:int=0, body_start:int=28
) -> str:
    """
Prints a formatted line of text, with a dot-leader between the 
lead and the line supplied
"""
    output = ''
    if indent:
        output = ' '*(3*(indent-1)) + '+- '
    output += leader
    if line:
        output = (
            (output + ' ').ljust(body_start - 1, '.') 
            + ' ' + line
        )
    print(output)

# - Create a basic list to use as a stack
my_stack = []
print_line('my_stack (initially)', str(my_stack))

# - "push" values into the stack with my_stack.append
my_stack.append(1)
my_stack.append(2)
my_stack.append(3)

print_line('my_stack (pushed 1,2,3)', str(my_stack))

# - pop a value from the stack
value = my_stack.pop()
print_line('value (popped)', str(value), 1)
print_line('my_stack (after pop)', str(my_stack))

# - Push a couple random values
new_value = randint(49,99)
my_stack.append(new_value)
print_line('my_stack (pushed %s)' % new_value, str(my_stack))
new_value = randint(1,49)
my_stack.append(new_value)
print_line('my_stack (pushed %s)' % new_value, str(my_stack))

# - Pop all values from the stack
while len(my_stack):
    value = my_stack.pop()
    print_line('value (popped)', str(value), 1)
    print_line('my_stack (after pop)', str(my_stack), 1)

# - Using a UserList to more tightly define a list-based 
#   stack-implementation

from collections import UserList

class stack(UserList):
    def push(self, value):
        self.data.append(value)
    def pop(self):
        return self.data.pop()
    def sort(self, *args, **kwargs):
        raise AttributeError(
            '%s instances are not sortable' % 
            self.__class__.__name__
        )
    def __setitem__(self, *args, **kwargs):
        raise RuntimeError(
            '%s instances cannot be altered except by '
            'using push' % 
            self.__class__.__name__
        )

empty_stack = stack()
print_line('empty_stack', str(empty_stack))
my_stack = stack([9,8,7,6,5,4,3,2,1])
print_line('my_stack', str(my_stack))
try:
    my_stack.sort()
except Exception as error:
    print_line(
        'my_stack.sort', '%s: %s' % 
        (error.__class__.__name__, error)
    )
try:
    my_stack[4] = 23
except Exception as error:
    print_line(
        'my_stack[4] = ', '%s: %s' % 
        (error.__class__.__name__, error)
    )
try:
    my_stack[4:5] = [99,98]
except Exception as error:
    print_line(
        'my_stack[4:5] = ', '%s: %s' % 
        (error.__class__.__name__, error)
    )
