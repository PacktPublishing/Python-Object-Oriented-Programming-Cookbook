#!/usr/bin/env python
"""
The complete code of Ch. 1, Recipe 2 -- List Comprehensions
"""

date_list = [
    datetime(1970, 1, 1),
    datetime(2038, 1, 19),
    datetime(1994, 1, 26),
    datetime(1998, 11, 25),
    datetime(1966, 9, 8),
    datetime(1969, 6, 3),
    datetime(1987, 9, 28),
    datetime(1994, 5, 23),
    datetime(1969, 7, 20),
    datetime(1972, 12, 11),
]

pangram = 'sphinx of black quartz judge my vow'
sentence = 'this is just a sentence'

if __name__ == '__main__':

    ### BASIC examples
    # A list comprehension can be built from any iterable:
    # - All the items in an existing list, for example, though 
    #   that's not likely to be of much use, since it just 
    #   results in a copy of the original list...
    all_dates = [d for d in date_list]
    print(all_dates == date_list)
    # - All the characters in a string -- strings are iterables 
    #   as well:
    pangram_chars = [c for c in pangram]
    sentence_chars = [c for c in sentence]
    print(pangram_chars)
    print(sentence_chars)

    ### MAPPING examples
    # - Examples of applying a function to each element of a 
    #   list, transforming it in the process, and returning a 
    #   new list of values with a list comprehension. This is 
    #   a mapping, equivalent to calling 
    #   map(lambda d: d.strftime(format), date_list)
    ymd_date_list = [
        date.strftime(ymd_format)
        for date in date_list
    ]
    print(ymd_date_list)

    dmy_date_list = [
        date.strftime(dmy_format)
        for date in date_list
    ]
    print(dmy_date_list)

    # - Any sequence-type (lists, tuples, strings, sets, etc.) 
    #   can be used as the "in" value:
    pangram_chars = [hex(ord(c)) for c in pangram]
    print(pangram_chars)

    sentence_chars = [c for c in sentence]
    print(sentence_chars)

    ### FILTERING examples
    # - Examples of applying criteria to each element as it's 
    #   being evaluated for inclusion in the new list generated 
    #   by the comprehension. This is filtering, equivalent to 
    #   calling 
    #   filter(lambda d: d.year>=1990 and d.year<2000, date_list)
    dates_1990s = [
        d for d in date_list
        if d.year>=1990 and d.year<2000
    ]
    print(dates_1990s)

    dates_1960s = [
        d for d in date_list
        if d.year>=1960 and d.year<1970
    ]
    print(dates_1960s)

    dates_1960s_90s = [
        d for d in date_list
        if (d.year>=1990 and d.year<2000)
        or (d.year>=1960 and d.year<1970)
    ]
    print(dates_1960s_90s)

    ### COMBINATION of MAPPING and FILTERING
    # - map AND filter equivalent:
    #   map(
    #       lambda m: m.strftime(ymd_format), 
    #       filter(
    #           lambda d: d.year>=1990 and d.year<2000, 
    #           date_list
    #       )
    #   )
    ymd_dates_1990s = [
        date.strftime(ymd_format)
        for date in date_list
        if date.year>=1990 and date.year<2000
    ]
    print(ymd_dates_1990s)

    dmy_dates_1960s = [
        date.strftime(dmy_format)
        for date in date_list
        if date.year>=1960 and date.year<1970
    ]
    print(dmy_dates_1990s)

