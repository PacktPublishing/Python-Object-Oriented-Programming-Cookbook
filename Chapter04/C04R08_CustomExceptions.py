#!/usr/bin/env python
"""
The complete code of Ch. 4, Recipe 7 -- 
Creating and using custom exceptions
"""

# - The bare-bones example, commented out so that this module 
#   can be executed and show the final error being raised
# class OutOfCheeseError(Exception):
#     pass

# if not cheese_count:
#     raise OutOfCheeseError(
#         'The current cheese count is %d' % cheese_count
#     )

class OutOfCheeseError(Exception):
    def __init__(self, msg, last_cheese=None):
        if last_cheese:
            msg += ': the last cheese was %s' % last_cheese
        self.msg = msg

class HTTPError(Exception):
    http_status = None
    http_message = None

    @property
    def status(self):
        return '%s %s' % (self.http_status, self.http_message)

    def __init__(self, *args, **kwargs):
        if not self.http_status or type(self.http_status) != int:
            raise AttributeError(
                '%s does not specify a numeric http_status '
                'value. Please specify a valid HTTP status '
                'code' % self.__class__.__name__
            )
        if not self.http_message or type(self.http_message) != str:
            raise AttributeError(
                '%s does not specify an http_message value. '
                'Please specify a valid HTTP status '
                'message' % self.__class__.__name__
            )
        Exception.__init__(self, *args, **kwargs)

class HTTP_400(HTTPError):
    http_status = 400
    http_message = 'Bad Request'

class HTTP_404(HTTPError):
    http_status = 404
    http_message = 'Not Found'


if __name__ == '__main__':
    ### DEMO CODE: Uncomment one of the following, then run the 
    ### script; then re-comment that item, and uncomment 
    ### something different to see how errors are handled...
    demo_error = None
#    demo_error = OutOfCheeseError
#    demo_error = RuntimeError
#    demo_error = TypeError
#    demo_error = ValueError

    try:
        print('Trying something that might raise errors...')
        if not demo_error:
            pass
        elif demo_error == OutOfCheeseError:
            cheese_count = 0
            current_cheese = 'Camembert'
            raise OutOfCheeseError(
                'The current cheese count is %d' % cheese_count,
                current_cheese
            )
        else:
            raise demo_error('%s raised' % demo_error.__name__)
    except RuntimeError:
        print('(runtime branch) RuntimeError caught')
        # - Re-raise the SAME error
        raise
    except (TypeError, ValueError) as error:
        print(
            '(type/value branch) %s caught: %s' % 
            (error.__class__.__name__, error)
        )
    except Exception as error:
        print(
            '%s caught (general exception handling): %s' % 
            (error.__class__.__name__, error)
        )
    else:
        print('(else branch) No error encountered')
    finally:
        print('(finally branch) Executing "finally" code')

    try:
        # - Uncomment one of these to raise a specific error
3        raise HTTP_400('This is a bad request')
#        raise HTTP_404('This request cannot be fulfilled')
        pass
    except HTTPError as error:
        print(
            '%s (%s): %s' % (
                error.__class__.__name__, error.status, 
                error
            )
        )
