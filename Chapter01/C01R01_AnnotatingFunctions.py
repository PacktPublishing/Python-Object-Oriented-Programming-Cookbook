#!/usr/bin/env python
"""
The complete code of Ch. 1, Recipe 1 -- Annotating Functions
"""

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

def all_arg_types(
    arg:str, 
    arg2:(bool,None)=None, 
    *args:(int,float), 
    kwdonly:str, 
    kwdonly2:(bool,None)=None, 
    **kwargs:type
) -> (str,None):
    print_line('all_arg_types called:')
    print_line('arg', str(arg), 1)
    print_line('arg2', str(arg2), 1)
    print_line('args', str(args), 1)
    print_line('kwdonly', str(kwdonly), 1)
    print_line('kwdonly2', str(kwdonly2), 1)
    print_line('kwargs:', None, 1)
    for kwdarg in kwargs:
        print_line(kwdarg, kwargs[kwdarg], 2)

if __name__ == '__main__':
    import sys
    # - Call the all_arg_types function
    all_arg_types(
        'first arg', True, 3.14, -1, kwdonly='kwdonly', 
        kwdonly2=None, key1='value1', key2='value2'
    )
    # - Examine the all_arg_types function
    print(all_arg_types)
    print_line('__annotations__:')
    for item in all_arg_types.__annotations__:
        print_line(item, 
            str(all_arg_types.__annotations__[item]), 1
        )
    # - Import getfullargspec from the inspect module
    from inspect import getfullargspec
    # - Get the full arg-spec of the annotated function
    argspec = getfullargspec(all_arg_types)
    print_line('fullargspec(%s):' % all_arg_types)
    print_line('varargs', str(argspec.varargs), 1)
    print_line('varkw', str(argspec.varkw), 1)
    print_line('defaults', str(argspec.defaults), 1)
    print_line('kwonlyargs', str(argspec.kwonlyargs), 1)
    print_line('kwonlydefaults', str(argspec.kwonlydefaults), 1)
    print_line('annotations', None, 1)
    for item in argspec.annotations:
        print_line(item, 
            str(argspec.annotations[item]), 2
        )
    # ~ # - Examine the print_line function
    print(print_line)
    print_line('__annotations__:')
    for item in print_line.__annotations__:
        print_line(item, 
            str(print_line.__annotations__[item]), 1
        )
    argspec = getfullargspec(print_line)
    print_line('fullargspec(%s):' % all_arg_types)
    print_line('varargs', str(argspec.varargs), 1)
    print_line('varkw', str(argspec.varkw), 1)
    print_line('defaults', str(argspec.defaults), 1)
    print_line('kwonlyargs', str(argspec.kwonlyargs), 1)
    print_line('kwonlydefaults', str(argspec.kwonlydefaults), 1)
    print_line('annotations', None, 1)
    for item in argspec.annotations:
        print_line(item, 
            str(argspec.annotations[item]), 2
        )

