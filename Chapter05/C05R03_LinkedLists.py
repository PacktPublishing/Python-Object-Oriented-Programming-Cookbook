#!/usr/bin/env python
"""
The complete code of Ch. 5, Recipe 3 -- 
Creating Linked Lists in Python
"""

o1=object()
o2=object()
o3=object()

example_list = [o1, o2, o3]
print(hex(id(example_list)))
print([hex(id(o)) for o in example_list])

o4=object()
o5=object()
o6=object()

example_list += [o6, o5, o4]
print(hex(id(example_list)))
print([hex(id(o)) for o in example_list])

class ListMember:
    """
Represents a member (or node) in a linked list.
Each member has a value, and keeps track of what the 
next member is.
"""
    def __init__(self, value):
        self.value = value
        self.next_item=None

    def __str__(self):
        return ('ListMember(value=%s)' % (self.value))

class LinkedList:
    """Provides a Linked List of members"""
    def __init__(self, *members):
        self.first_member = None
        self.last_member = None
        for member in members:
            self.append(member)

    def append(self, member):
        new_member = ListMember(member)
        if self.last_member == None:
            # - Since self.last_member is None, we have to 
            #   create the first_member value
            self.first_member = new_member
            # - At this point, the first member is also the 
            #   last member, so keep track of that too...
            self.last_member = new_member
        else:
            # - Since we have a last_member in this branch, 
            #   we need to set its next_item to the new member:
            self.last_member.next_item = new_member
            # - Then re-set self.last_member to point to the 
            #   *new* last_member:
            self.last_member = new_member

    def __iter__(self):
        if not self.first_member:
            raise StopIteration
        else:
            self.__iteritem = self.first_member
            return self

    def __next__(self):
        if self.__iteritem:
            result = self.__iteritem
            self.__iteritem = self.__iteritem.next_item
            return result
        raise StopIteration


class IndexedLinkedList(LinkedList):
    """
Extends LinkedList to allow retrieval of members by a numeric index
"""
    def __getitem__(self, index:int):
        for i in range(0,index):
            if i == 0:
                current_item = self.first_member
            else:
                try:
                    current_item = current_item.next_item
                except AttributeError:
                    raise IndexError('list index out of range')
        return current_item

class ArrayMember:
    """
Represents a member (or node) in a linked list.
Each member has a value, and keeps track of what the 
next member is.
"""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next_item=None

    def __str__(self):
        return (
            'ListMember(key=%s value=%s)' % 
            (self.key, self.value)
        )

class AssociativeArray(LinkedList):

    def append(self, member):
        new_member = ArrayMember(member)
        if self.last_member == None:
            # - Since self.last_member is None, we have to 
            #   create the first_member value
            self.first_member = new_member
            # - At this point, the first member is also the 
            #   last member, so keep track of that too...
            self.last_member = new_member
        else:
            # - Since we have a last_member in this branch, 
            #   we need to set its next_item to the new member:
            self.last_member.next_item = new_member
            # - Then re-set self.last_member to point to the 
            #   *new* last_member:
            self.last_member = new_member

    def __getitem__(self, index):
        if type(index) == int:
            for i in range(0,index):
                if i == 0:
                    current_item = self.first_member
                else:
                    try:
                        current_item = current_item.next_item
                    except AttributeError:
                        raise IndexError(
                            'list index out of range'
                        )
            return current_item
        else:
            current_item = self.first_member
            while current_item:
                if current_item.key == index:
                    return current_item
                current_item = current_item.next_item
            raise KeyError(index)


if __name__ == '__main__':

    print('LinkedList example')
    my_list = LinkedList(1,2,3)
    print(my_list)
    current_item = my_list.first_member
    while current_item:
        print(current_item)
        current_item = current_item.next_item

    print('__iter__ results')
    for i in my_list:
        print(i)

    print('Basis for a search:')
    search_results = [str(i) for i in my_list if i.value == 2]
    print(search_results)

    print('Basis for filtering:')
    filter_results = [str(i) for i in my_list if i.value % 2]
    print(filter_results)

    print('IndexedLinkedList example')
    my_list = IndexedLinkedList(1,2,3)
    print(my_list)
    print(my_list.last_member)
    current_item = my_list.first_member
    while current_item:
        print(current_item)
        current_item = current_item.next_item
    print(my_list[1])
