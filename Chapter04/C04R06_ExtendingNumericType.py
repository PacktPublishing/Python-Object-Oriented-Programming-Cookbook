#!/usr/bin/env python
"""
The complete code of Ch. 4, Recipe 6 -- 
Extending built-in types: Ipv4Address revisited
"""

class IPv4Address(int):
    """Represents an IPv4 Address"""

    _min_range = 0
    _max_range = 256**4-1

    def __new__(cls, *args, **kwargs):
        # - The first item in *args is the value of the int, 
        #   so we need to extract that to allow for non-int 
        #   values. We're preserving any other args, just in 
        #   case they are needed later.
        value = args[0]
        args = args[1:]
        # - Handle the incoming value, converting if needed
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
            if value < cls._min_range or value > cls._max_range:
                raise ValueError()
        else:
            raise TypeError()
        # - Delegate to superclass for actual object-creation. 
        #   Note that value is being passed explicitly
        instance = super().__new__(cls, value, *args, **kwargs)
        # - Return the new instance
        return instance

    def __str__(self):
        octets = []
        value = super().__int__()
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

    # - Other methods that complete the numeric-type functionality
    def __add__ (self, other):
        result = super().__int__() + int(other)
        if result < self._min_range or result > self._max_range:
            raise ValueError(
                'The result of this operation would result in an '
                'invalid IPv4 address'
            )
        return IPv4Address(result)

    def __sub__ (self, other):
        result = super().__int__() - int(other)
        if result < self._min_range or result > self._max_range:
            raise ValueError(
                'The result of this operation would result in an '
                'invalid IPv4 address'
            )
        return IPv4Address(result)

    def __mul__ (self, other):
        result = super().__int__() * int(other)
        if result < self._min_range or result > self._max_range:
            raise ValueError(
                'The result of this operation would result in an '
                'invalid IPv4 address'
            )
        return IPv4Address(result)

    def __div__ (self, other):
        result = super().__int__() / int(other)
        if result < self._min_range or result > self._max_range \
            or type(result) != int:
            raise ValueError(
                'The result of this operation would result in an '
                'invalid IPv4 address'
            )
        return IPv4Address(result)

    def __mod__ (self, other):
        result = super().__int__() % int(other)
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
        result = super().__int__() >> int(other)
        if result < self._min_range or result > self._max_range:
            raise ValueError(
                'The result of this operation would result in an '
                'invalid IPv4 address'
            )
        return IPv4Address(result)

    def __and__ (self, other):
        result = super().__int__() & int(other)
        if result < self._min_range or result > self._max_range:
            raise ValueError(
                'The result of this operation would result in an '
                'invalid IPv4 address'
            )
        return IPv4Address(result)

    def __or__ (self, other):
        result = super().__int__() | int(other)
        if result < self._min_range or result > self._max_range:
            raise ValueError(
                'The result of this operation would result in an '
                'invalid IPv4 address'
            )
        return IPv4Address(result)

    def __xor__ (self, other):
        result = super().__int__() ^ int(other)
        if result < self._min_range or result > self._max_range:
            raise ValueError(
                'The result of this operation would result in an '
                'invalid IPv4 address'
            )
        return IPv4Address(result)

if __name__ == '__main__':

    ip1 = IPv4Address('127.0.0.1')
    ip2 = IPv4Address(1000000001)

    print('ip1 .......... %s' % ip1)
    print('int(ip1) ..... %d' % ip1)
    print('ip2 .......... %s' % ip2)
    print('int(ip2) ..... %d' % ip2)

    ip3 = IPv4Address('127.0.0.1')
    ip3 += 1
    ips = [
        IPv4Address(ip) for ip in 
        ('10.0.0.0', '192.168.0.0', '127.0.0.1')
    ]

    print('ip3 .......... %s' % ip3)
    print('int(ip3) ..... %d' % ip3)
    print('ip2 == ip3 ... %s' % (ip2 == ip3))
    print('ip2 < ip3 .... %s' % (ip2 < ip3))
    print('ip2 > ip3 .... %s' % (ip2 > ip3))
    print(ips)

    ips_sorted = sorted(ips, key=lambda ip:int(ip))
    print(ips_sorted)

    # - One of the basics of determining whether one IPv4 address is 
    #   in a network range is available just by using a boolean AND 
    #   operation between the two, but there is a binary mask (the 
    #   "24" in "10.0.0.0/24") that would have to be applied in some 
    #   fashion that would make it equivalent to 10.255.255.255:
#    my_ip = IPv4Address('10.1.100.40')
#    ip_range = IPv4Address('10.255.255.255')
#    print(
#        'my IP (%s) in IP range (%s): %s' % 
#        (my_ip, ip_range, True if my_ip & ip_range else False)
#    )
#    ip_range = IPv4Address('10.5.255.255')
#    print(
#        'my IP (%s) in IP range (%s): %s' % 
#        (my_ip, ip_range, True if my_ip & ip_range else False)
#    )

    print('-'*80)
    ip=IPv4Address('255.255.255.255')
    ip += 1
    print(ip)
