#!/usr/bin/env python
"""
The complete code of Ch. 4, Recipe 4 -- 
Emulating a numeric type with magic methods
"""

class IPv4Address:
    """Represents an IPv4 Address"""

    _min_range = 0
    _max_range = 256**4-1

    def __init__(self, value:(int,str)):
        if type(value) == str:
            octets = [int(o) for o in value.split('.')[0:4]]
            if len(octets) != 4:
                raise ValueError()
            octets.reverse()
            value = sum(
                [
                    value * 256**power for (power, value) 
                    in enumerate(octets)
                ]
            )
        if type(value) == int:
            if value < self._min_range or value > self._max_range:
                raise ValueError()
            self._int_value = value
        else:
            raise TypeError()

    def __str__(self):
        octets = []
        value = self._int_value
        for power in range(0,4):
            octet, value = (value % 256, int(value/256))
            octets.insert(0, octet)
        return '.'.join([str(o) for o in octets])

    def __repr__(self):
        return (
            '<%s at %s (%s)>' % 
            (
                self.__class__.__name__, hex(id(self)), 
                self.__str__()
            )
        )

    def __int__(self):
        return self._int_value

    # - Other methods that complete the numeric-type emulation
    def __add__ (self, other):
        result = self._int_value + int(other)
        if result < self._min_range or result > self._max_range:
            raise ValueError(
                'The result of this operation would result in an '
                'invalid IPv4 address'
            )
        return IPv4Address(result)

    def __sub__ (self, other):
        result = self._int_value - int(other)
        if result < self._min_range or result > self._max_range:
            raise ValueError(
                'The result of this operation would result in an '
                'invalid IPv4 address'
            )
        return IPv4Address(result)

    def __mul__ (self, other):
        result = self._int_value * int(other)
        if result < self._min_range or result > self._max_range:
            raise ValueError(
                'The result of this operation would result in an '
                'invalid IPv4 address'
            )
        return IPv4Address(result)

    def __div__ (self, other):
        result = self._int_value / int(other)
        if result < self._min_range or result > self._max_range \
            or type(result) != int:
            raise ValueError(
                'The result of this operation would result in an '
                'invalid IPv4 address'
            )
        return IPv4Address(result)

    def __mod__ (self, other):
        result = self._int_value % int(other)
        if result < self._min_range or result > self._max_range:
            raise ValueError(
                'The result of this operation would result in an '
                'invalid IPv4 address'
            )
        return IPv4Address(result)

    def __lshift__ (self, other):
        result = self._int_value << int(other)
        if result < self._min_range or result > self._max_range:
            raise ValueError(
                'The result of this operation would result in an '
                'invalid IPv4 address'
            )
        return IPv4Address(result)

    def __rshift__ (self, other):
        result = self._int_value >> int(other)
        if result < self._min_range or result > self._max_range:
            raise ValueError(
                'The result of this operation would result in an '
                'invalid IPv4 address'
            )
        return IPv4Address(result)

    def __and__ (self, other):
        result = self._int_value & int(other)
        if result < self._min_range or result > self._max_range:
            raise ValueError(
                'The result of this operation would result in an '
                'invalid IPv4 address'
            )
        return IPv4Address(result)

    def __xor__ (self, other):
        result = self._int_value ^ int(other)
        if result < self._min_range or result > self._max_range:
            raise ValueError(
                'The result of this operation would result in an '
                'invalid IPv4 address'
            )
        return IPv4Address(result)

    def __or__ (self, other):
        result = self._int_value | int(other)
        if result < self._min_range or result > self._max_range:
            raise ValueError(
                'The result of this operation would result in an '
                'invalid IPv4 address'
            )
        return IPv4Address(result)

if __name__ == '__main__':

    # - Basic object-creation
    ip = IPv4Address('127.0.0.1')
    print('ip._int_value ... %s' % ip._int_value)
    print('int(ip) ......... %s' % int(ip))
    print('ip .............. %s' % ip)

    # - Arithmetic opersions: addition
    ip += 2
    print('int(ip) ......... %s' % int(ip))
    print('ip .............. %s' % ip)
    #   ...subtraction
    ip -= 1
    print('int(ip) ......... %s' % int(ip))
    print('ip .............. %s' % ip)

    # - Instance-creation with an int argument
    ip = IPv4Address(270000000)
    print('int(ip) ......... %s' % int(ip))
    print('ip .............. %s' % ip)

    # - One of the basics of determining whether one IPv4 address is 
    #   in a network range is available just by using a boolean AND 
    #   operation between the two, but there is a binary mask (the 
    #   "24" in "10.0.0.0/24") that would have to be applied in some 
    #   fashion that would make it equivalent to 10.255.255.255:
    my_ip = IPv4Address('10.1.100.40')
    ip_range = IPv4Address('10.0.0.0')
    print(
        'my IP (%s) in IP range (%s): %s' % 
        (my_ip, ip_range, True if int(my_ip & ip_range) else False)
    )
    ip_range = IPv4Address('192.0.0.0')
    print(
        'my IP (%s) in IP range (%s): %s' % 
        (my_ip, ip_range, True if int(my_ip & ip_range) else False)
    )

    ips = [
        IPv4Address(ip) for ip in 
        ('10.0.0.0', '192.168.0.0', '127.0.0.1')
    ]
    print(ips)

    ips = sorted(ips, key=lambda ip:int(ip))
    print(ips)

    try:
        ips = sorted(ips)
    except Exception as error:
        print('%s: %s' % (error.__class__.__name__, error))
