#!/usr/bin/env python
"""
The complete code of Ch. 1, Recipe 6 -- Decorators with Arguments
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

def doesnt_work(*args):
    print_line('Calling doesnt_work')
    print_line('args', str(args),1)
    def _decorator(*args, **kwargs):
        print_line('Calling doesnt_work')
        print_line('args', str(args),2)
        return decorated_item(*args, **kwargs)
    print_line('Returning', str(_decorator))
    return _decorator

# - A decorator with arguments operates in three steps. 
#   The first is the outer decorator call: 
#   @decorator(arguments)
def decorator(*args, **kwargs):
    print_line('decorator called:')
    print_line('args', str(args), 1)
    print_line('kwargs', str(kwargs), 1)
    # - The second is the "real" decorator-function, that 
    #   accepts *only* the element being decorated 
    #   (decorated_item):
    def _decorator(decorated_item):
        print_line('_decorator called:', None, 2)
        print_line('decorated_item', str(decorated_item), 3)
        # - The third is the "real" decoration, which has 
        #   access to all of the decorator and _decorator 
        #   arguments:
        def inner_decorator(*iargs, **ikwargs):
            # - Do something with the decorated item (which 
            #   can use the outer decorator's arguments even 
            #   apart from decorated_item). 
            #   For now, just call the original decorated 
            #   function (with the inner_decorator arguments):
            print_line('inner_decorator called:', None, 4)
            print_line('decorated_item', str(decorated_item), 5)
            print_line('args', str(args), 5)
            print_line('kwargs', str(kwargs), 5)
            print_line('iargs', str(iargs), 5)
            print_line('ikwargs', str(ikwargs), 5)
            decorated_item(*iargs, **ikwargs)
        print_line('inner_decorator', str(inner_decorator), 3)
        return inner_decorator
    print_line('_decorator', str(_decorator), 1)
    return _decorator

def document_arg(name, description):
    print_line('document_arg called:', None, 1)
    print_line('name', str(name), 2)
    print_line('description', str(description), 2)
    def _decorator(func):
        # - Since this decorator is adding data to the 
        #   __annotations__ of the target function (func), 
        #   all it needs to do is make those additions...
        try:
            # - Try to add the description to 
            #   func.__annotations__['__doc__']
            func.__annotations__['__doc__'][name] = description
        except KeyError:
            # - If __annotations__['__doc__'] doesn't exist, 
            #   create it with the only item provided so far
            func.__annotations__['__doc__']={name:description}
        #   ... and return the *original* function.
        return func
    return _decorator

def format_line(
    leader:str, line:(str,None)=None, 
    indent:int=0, body_start:int=28
):
    """
Returns a formatted line of text, with a dot-leader between the 
lead and the line supplied
"""
    output = ''
    if indent:
        output = ' '*(3*indent) + '+- '
    else:
        output = '+- '
    output += leader
    if line:
        output = (
            (output + ' ').ljust(body_start - 1, '.') 
            + ' ' + line
        )
    return output

def detailed_docs(target):
    # - Start by acquiring the original doc-string of the target
    result = (' '.join(
        [line.strip() for line in target.__doc__ .split('\n')]
    ) or 'No documentation defined').strip()
    # - Look for annotations, and build the argument 
    #   documentation if we can
    if target.__annotations__:
        _docitems = target.__annotations__.get('__doc__')
        if _docitems:
            result += '\n\nArguments:\n'
            for item in _docitems:
                item_types = target.__annotations__.get(item)
                if item_types:
                    if type(item_types) == tuple:
                        if len(item_types):
                            item_types = '|'.join([t.name for t in item_types])
                    else:
                        item_types = item_types.__name__
                else:
                    item_types = 'Not specified'
                result += format_line(item, '(%s) %s\n' % (item_types, _docitems[item]), 0, 24)
    return result

if __name__ == '__main__':

    # ~ try:
        # ~ @doesnt_work('decorating')
        # ~ def decorated(*args, **kwargs):
            # ~ print_line('decorated called:', None, 1)
            # ~ print_line('args', str(args), 2)
            # ~ print_line('kwargs', str(kwargs), 2)
    # ~ except NameError as error:
        # ~ print_line(
            # ~ 'Raises', '%s: %s' % (error.__class__.__name__, error)
        # ~ )

    # ~ print_line(
        # ~ 'Decorating a function with decorator (%s)' % 
        # ~ decorator
    # ~ )
    # ~ @decorator('decorating decorated', keys=True)
    # ~ def decorated(*args, **kwargs):
        # ~ print_line('decorated called:', None, 1)
        # ~ print_line('args', str(args), 2)
        # ~ print_line('kwargs', str(kwargs), 2)
    # ~ print_line('decorated', str(decorated))

    # ~ decorated('arg1', 'arg2', key1='value1')

    @document_arg('name', 'The name of the item')
    @document_arg(
        'active', 'Flag indicating whether the item is active '
            '(True) or not (False)'
    )
    def documented_function(name:str, active:bool=True) -> None:
        """
    The original docstring of the function.
        """
        pass

    # ~ from inspect import getfullargspec

    # ~ print(documented_function)
    # ~ print_line('__annotations__:')
    # ~ for item in documented_function.__annotations__:
        # ~ print_line(item, 
            # ~ str(documented_function.__annotations__[item]), 1
        # ~ )
    # ~ argspec = getfullargspec(documented_function)
    # ~ print_line('fullargspec(%s):' % documented_function)
    # ~ print_line('varargs', str(argspec.varargs), 1)
    # ~ print_line('varkw', str(argspec.varkw), 1)
    # ~ print_line('defaults', str(argspec.defaults), 1)
    # ~ print_line('kwonlyargs', str(argspec.kwonlyargs), 1)
    # ~ print_line('kwonlydefaults', str(argspec.kwonlydefaults), 1)
    # ~ print_line('annotations', '(See __annotations__, above)', 1)

    # ~ print(detailed_docs(documented_function))

    # ~ print('Calling decorated function (%s)' % decorated)
    # ~ decorated('decorated', decoration=True)

    # ~ print('Calling decorated2 function (%s)' % decorated2)
    # ~ decorated2('decorated2', decoration=True)

