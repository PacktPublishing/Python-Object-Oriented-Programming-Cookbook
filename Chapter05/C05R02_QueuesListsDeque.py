#!/usr/bin/env python
"""
The complete code of Ch. 5, Recipe 2 -- 
Queueing options: Lists and deques
"""

from collections import deque
from random import randint
from time import time

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

my_queue = deque([3,2,1])
print_line('my_queue (populated)', str(my_queue))
my_queue = deque()
print_line('my_queue (empty)', str(my_queue))

# - "push" values into the queue with my_queue.append
my_queue.append(1)
my_queue.append(2)
my_queue.append(3)

print_line('my_queue (pushed 1,2,3)', str(my_queue))

# - pop a value from the queue
value = my_queue.popleft()
print_line('value (popped)', str(value), 1)
print_line('my_queue (after pop)', str(my_queue))

# - Push a couple random values
new_value = randint(49,99)
my_queue.append(new_value)
print_line('my_queue (pushed %s)' % new_value, str(my_queue))
new_value = randint(1,49)
my_queue.append(new_value)
print_line('my_queue (pushed %s)' % new_value, str(my_queue))

print_line('deque iterable members')
print_line('len(my_queue)', str(len(my_queue)), 1)
print_line('my_queue[1]', str(my_queue[1]), 1)

# - Iterate over all members and show their values
print('Members of my_queue:')
for value in my_queue:
    print_line('item value', str(value), 1)

# - Pop all values from the queue
print('Popping all members in a while loop')
while my_queue:
    value = my_queue.popleft()
    print_line('value (popped)', str(value), 1)
    print_line('my_queue (after pop)', str(my_queue), 1)

