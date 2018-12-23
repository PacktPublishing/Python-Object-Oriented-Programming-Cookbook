#!/usr/bin/env python
"""
The complete code of Ch. 1, Recipe 5 -- Anatomy of a Decorator
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

# - A bare-bones decorator accepts just the decorated item as 
#   its sole argument
def decorator(decorated_item):
    print('#' + '-'*64 + '#')
    print_line('decorator called:')
    print_line('decorated_item', str(decorated_item), 1)
    def inner_decorator(*iargs, **ikwargs):
        print_line('inner_decorator called:', None,)
        print_line('decorated_item', str(decorated_item), 1)
        print_line('iargs', str(iargs), 1)
        print_line('ikwargs', str(ikwargs), 1)
        # - Do something with the decorated item (which might 
        #   use the outer decorator's arguments even apart 
        #   from decorated_item). For now, just call the 
        #   original decorated function:
        return decorated_item(*iargs, **ikwargs)
    print_line('inner_decorator', str(inner_decorator))
    print('#' + '-'*64 + '#')
    return inner_decorator

# - Decorating classes is possible too:
def class_wrapper(decorated_item):
    def inner_wrapper():
        # - Arguments for an inner-decorator class could be 
        #   difficult to manage, but it's doable... just 
        #   potentially complicated.
        class class_wrapper:
            def __init__(self, original_class):
                self.original_class = original_class
        # - Return here is the inner-decorator *class*
        return class_wrapper(decorated_item)
    # - Return here is the decorator *function*
    return inner_wrapper

# - Multiple decorators to show how application of more than one 
#   decorator executes.
def decorator_1(decorated_item):
    print_line('decorator_1 called:')
    print_line('decorated_item', str(decorated_item), 1)
    def inner_decorator(*iargs, **ikwargs):
        print_line('Calling decorator_1.inner_decorator')
        # - Do something with the decorated item (which might 
        #   use the outer decorator's arguments even apart 
        #   from decorated_item). For now, just call the 
        #   original decorated function:
        return decorated_item(*iargs, **ikwargs)
    return inner_decorator

def decorator_2(decorated_item):
    print_line('decorator_2 called:')
    print_line('decorated_item', str(decorated_item), 1)
    def inner_decorator(*iargs, **ikwargs):
        print_line('Calling decorator_2.inner_decorator')
        # - Do something with the decorated item (which might 
        #   use the outer decorator's arguments even apart 
        #   from decorated_item). For now, just call the 
        #   original decorated function:
        return decorated_item(*iargs, **ikwargs)
    return inner_decorator

def decorator_3(decorated_item):
    print_line('decorator_3 called:')
    print_line('decorated_item', str(decorated_item), 1)
    def inner_decorator(*iargs, **ikwargs):
        print_line('Calling decorator_3.inner_decorator')
        # - Do something with the decorated item (which might 
        #   use the outer decorator's arguments even apart 
        #   from decorated_item). For now, just call the 
        #   original decorated function:
        return decorated_item(*iargs, **ikwargs)
    return inner_decorator

if __name__ == '__main__':

    print_line('Decorating decorated w/', str(decorator))
    @decorator
    def decorated(*args, **kwargs):
        print_line('decorated called:', None, 1)
        print_line('args', str(args), 2)
        print_line('kwargs', str(kwargs), 2)
    print('decorated: %s' % decorated)

    print('Calling decorated function (%s)' % decorated)
    decorated('decorated', decoration=True)

    @decorator
    def decorated2(*args, **kwargs):
        print_line('decorated2 called:', None, 1)
        print_line('args', str(args), 2)
        print_line('kwargs', str(kwargs), 2)
    print('decorated2: %s' % decorated2)

    print('Calling decorated2 function (%s)' % decorated2)
    decorated2('decorated2', decoration=True)

    # - Name-checking example
    def name_must_be_string(decorated_item):
        def name_check(name):
            if type(name) != str:
                raise TypeError(
                    '%s expects a string value for its name '
                    'argument, but was passed "%s" (a %s)' % 
                    (
                        decorated_item.__name__, name, 
                        type(name).__name__
                    )
                )
            return decorated_item(name)
        return name_check

    @name_must_be_string
    def set_name(name):
        print_line('set_name', name)

    @name_must_be_string
    def do_something_with_name(name):
        print_line('do_something_with_name', name)

    @name_must_be_string
    def do_something_else_name(name):
        print_line('do_something_else_name', name)

    set_name('John Sheridan')
    do_something_with_name('Londo Mollari')
    do_something_else_name('Kosh Naranek')
    try:
        set_name(3.14)
    except TypeError as error:
        print(
            '%s (expected): %s' % 
            (error.__class__.__name__, error)
        )
    try:
        do_something_with_name(3.14)
    except TypeError as error:
        print(
            '%s (expected): %s' % 
            (error.__class__.__name__, error)
        )
    try:
        do_something_else_name(3.14)
    except TypeError as error:
        print(
            '%s (expected): %s' % 
            (error.__class__.__name__, error)
        )

    @class_wrapper
    class wrap_me:
        pass

    instance = wrap_me()
    print_line('instance', str(instance))
    print_line(
        'instance.original_class', str(instance.original_class)
    )

    print('='*80)

    @decorator_1
    @decorator_2
    @decorator_3
    def multiple_decorations(*args, **kwargs):
        print_line('multiple_decorations called:', None, 1)
        print_line('args', str(args), 2)
        print_line('kwargs', str(kwargs), 2)

    print('Calling multiple_decorations (%s)' % multiple_decorations)
    multiple_decorations('multiple_decorations', decoration=True)
