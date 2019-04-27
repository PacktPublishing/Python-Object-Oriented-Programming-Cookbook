#!/usr/bin/env python
"""
The complete code of Ch. 4, Recipe 5 -- 
Emulating a string type with magic methods
"""

class EmailAddress:

    @property
    def address(self):
        """Gets or sets the actual email address"""
        return self._address

    @address.setter
    def address(self, value):
        if type(value) != str:
            raise TypeError()
        value = value.strip()
        bad_chars = [c for c in value if ord(c)<32 or ord(c)>126]
        if not value:
            if bad_chars:
                raise ValueError('Invalid characters in address')
            else:
                raise ValueError('Invalid address')
        # TODO: Work out a well-formed-email-address validation 
        #       process and apply it here, raising a ValueError 
        #       if the supplied address is not at least well-
        #       formed. See https://emailregex.com/ as a 
        #       possible starting-point?
        self._address = value

    @property
    def name(self):
        """Gets, sets or deletes the name"""
        try:
            return self._name
        except AttributeError:
            return None

    @name.setter
    def name(self, value):
        if value != None:
            if type(value) != str:
                raise TypeError()
            value = value.strip()
            bad_chars = [c for c in value if ord(c)<32 or ord(c)>126]
            if not value:
                if bad_chars:
                    raise ValueError('Invalid characters in name')
                else:
                    raise ValueError('Invalid name')
        self._name = value

    @name.deleter
    def name(self):
        try:
            del self._name
        except AttributeError:
            pass

    def __init__(self, value):
        # - Make sure we're dealing with either a string or an 
        #   instance of the class
        if type(value) not in (str, self.__class__):
            raise TypeError()
        # - Convert it to a string value to work with
        value = str(value)
        # - Start by assuming that the address is valid
        is_valid = True
        # - Break it into its components:
        #   - email.address@domain.com
        #   - User Name <email.address@domain.com>
        if '<' in value and value.strip().endswith('>'):
            try:
                self.name, self.address = [
                    s.strip() for s in value.split('<')
                ]
                self.address = self.address[0:-1]
            except ValueError:
                # - Too many values to unpack
                is_valid = False
        else:
            self.address = value

    def __str__(self):
        if self.name:
            return '%s <%s>' % (self.name, self.address)
        return self.address

    def __repr__(self):
        return '%s(%s)' % (self.__class__.__name__, str(self))

    # - Magic and non-magic methods that provide string-type 
    #   emulation capabilities

    def __contains__(self, item):
        return str(self).__contains__(item)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            other = str(other)
        return str(self) == other

    def __ge__(self, other):
        if isinstance(other, self.__class__):
            other = str(other)
        return str(self) >= other

    def __gt__(self, other):
        if isinstance(other, self.__class__):
            other = str(other)
        return str(self) > other

    def __le__(self, other):
        if isinstance(other, self.__class__):
            other = str(other)
        return str(self) <= other

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            other = str(other)
        return str(self) < other

    def __neq__(self, other):
        if isinstance(other, self.__class__):
            other = str(other)
        return str(self) != other

    def index(self, sub, *args):
        return str(self).index(sub, *args)

    # - Other string-related methods that don't make much sense 
    #   to implement, because they would either return invalid 
    #   values, or values of different types.

    def __add__(self, other):
        if isinstance(other, self.__class__):
            other = str(other)
        return EmailAddress(str(self) + other)

#    def __getitem__(self, index):
#        return str(self).__getitem__(index)

#    def __iter__(self):
#        return str(self).__iter__()

#    def __len__(self):
#        return len(str(self))

if __name__ == '__main__':
    my_address=EmailAddress('someone@gmail.com')
    print(my_address)
    my_address.name = 'Brian Allbee'
    print(my_address)

    my_address=EmailAddress('Brian Allbee <someone@gmail.com>')
    print(my_address)
    print(my_address.name)
    print(my_address.address)

    addr1 = EmailAddress('someone@gmail.com')
    addr2 = EmailAddress('someone-else@gmail.com')
    print('addr1 == addr2 ... %s' % (addr1 == addr2))
    print('addr1 < addr2 .... %s' % (addr1 < addr2))
    print('addr1 > addr2 .... %s' % (addr1 > addr2))
    addr_list = [addr1, addr2]
    addr_list.sort()
    print(addr_list)

    print('gmail' in my_address)
    print(my_address.index('gmail'))

    addr1 = EmailAddress('someone@gmail.com')
    addr1 += EmailAddress('someone-else@gmail.com')
    print(addr1)
    print(type(addr1))
