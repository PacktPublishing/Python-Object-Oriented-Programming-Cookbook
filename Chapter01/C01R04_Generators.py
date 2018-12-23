#!/usr/bin/env python
"""
The complete code of Ch. 1, Recipe 4 -- Generators
"""

import math

from datetime import datetime

ymd_format = '%Y-%m-%d'
dmy_format = '%d %b %Y'

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

if __name__ == '__main__':
    # - Create the date-list generator
    all_dates = (
        d.strftime(ymd_format) for d in date_list
        if d.year>=1990 and d.year<2000
    )
    # - Print it to show that it's not a list, tuple, etc.
    print(all_dates)
    # - But it can still be iterated against
    for date in all_dates:
        print(date)

    # - A prime-number-finding function that returns a list 
    #   of values
    def prime_numbers_list(start, end):
        result = []
        number = start
        while number <= end:
            limit = math.sqrt(number)
            factors = [
                n for n in range(1, int(limit+1))
                if int(number/n) == number/n
            ]
            if len(factors) == 1:
                result.append(number)
            number += 1
        return result
    # - Get prime_numbers results for the same ranges of numbers, 
    #   and print them
    primes_2_30 = prime_numbers_list(2,30)
    primes_100_150 = prime_numbers_list(100,150)
    print(primes_2_30)
    print(primes_100_150)

    # - A prime-number-finding function that returns a 
    #   *generator* of member-values
    def prime_numbers(start, end):
        number = start
        while number <= end:
            limit = math.sqrt(number)
            factors = [
                n for n in range(1, int(limit+1))
                if int(number/n) == number/n
            ]
            if len(factors) == 1:
                # NOTE: We're using yield here!
                yield number
            number += 1

    # - prime_numbers still looks like a standard function, 
    #   externally:
    print(prime_numbers)
    print(type(prime_numbers))
    # - Get prime_numbers results for the same ranges of numbers, 
    #   and print them
    primes_2_30 = prime_numbers(2,30)
    primes_100_150 = prime_numbers(100,150)
    # - The results are generators, though:
    print(primes_2_30)
    print(primes_100_150)
    # - The entire result-set can be retrieved as a list if needed
    print(list(primes_2_30))
    print(list(primes_100_150))

