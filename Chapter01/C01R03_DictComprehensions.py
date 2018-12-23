#!/usr/bin/env python
"""
The complete code of Ch. 1, Recipe 3 -- Dictionary Comprehensions
"""

from datetime import datetime

ymd_format = '%Y-%m-%d'
dmy_format = '%d %b %Y'

events = {
    'UNIX Epoch Start': datetime(1970, 1, 1),
    'UNIX Epoch End': datetime(2038, 1, 19),
    'B5 First Episode':datetime(1994, 1, 26),
    'B5 Last Episode':datetime(1998, 11, 25),
    'ST:TOS First Episode':datetime(1966, 9, 8),
    'ST:TOS Last Episode':datetime(1969, 6, 3),
    'ST:TNG First Episode':datetime(1987, 9, 28),
    'ST:TNG Last Episode':datetime(1994, 5, 23),
    'First Moon Landing':datetime(1969, 7, 20),
    'Last Moon Landing':datetime(1972, 12, 11),
}

if __name__ == '__main__':

    from pprint import pprint

    ### MAPPING examples
    # - Examples of applying a function to each element of a 
    #   list, transforming it in the process, and returning a 
    #   new dict of values with a dict comprehension. 
    ymd_date_dict = {
        key:events[key].strftime(ymd_format)
        for key in events
    }
    pprint(ymd_date_dict)

    dmy_date_dict = {
        key:events[key].strftime(dmy_format)
        for key in events
    }
    pprint(dmy_date_dict)

    ### FILTERING examples
    # - Examples of applying criteria to each element as it's 
    #   being evaluated for inclusion in the new dict generated 
    #   by the comprehension. 
    sf_dates_dict = {
        key:events[key]
        for key in events
        if key.startswith('ST:') or key.startswith('B5')
    }
    pprint(sf_dates_dict)

    ### COMBINATION of MAPPING and FILTERING
    sf_dates_dict = {
        key:events[key].strftime(ymd_format)
        for key in events
        if key.startswith('ST:') or key.startswith('B5')
    }
    pprint(sf_dates_dict)
