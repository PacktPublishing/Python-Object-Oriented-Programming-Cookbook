#!/usr/bin/env python
"""
The complete code of Ch. 5, Recipe 5 -- 
Creating Data-trees in Python
"""

class Node:
    """
Provides a (very) simple tree data-structure, where each node 
is allowed to have a "left" and "right" node (also Node 
instances)
    """

    @property
    def left_node(self):
        try:
            return self._left_node
        except AttributeError:
            return None

    @left_node.setter
    def left_node(self, value):
        if value != None:
            if not isinstance(value, self.__class__):
                raise TypeError(
                    '%s.left_node expects an instance of Node, '
                    'but was passed "%s" (%s)' % (
                        self.__class__.__name__, value, 
                        type(value).__name__
                    )
                )
        self._left_node = value

    @left_node.deleter
    def left_node(self):
        try:
            del self._left_node
        except AttributeError:
            pass

    @property
    def right_node(self):
        try:
            return self._right_node
        except AttributeError:
            return None

    @right_node.setter
    def right_node(self, value):
        if value != None:
            if not isinstance(value, self.__class__):
                raise TypeError(
                    '%s.right_node expects an instance of Node, '
                    'but was passed "%s" (%s)' % (
                        self.__class__.__name__, value, 
                        type(value).__name__
                    )
                )
            self._right_node = value

    @right_node.deleter
    def right_node(self):
        try:
            del self._right_node
        except AttributeError:
            pass

    def __init__(self, data, left_node=None, right_node=None):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node

    def __str__(self):
        return 'Node(data=%s)' % self.data

    def print_tree(self, indent=0):
        if not indent:
            print(self)
        else:
            print(' '*(3 * (indent-1)) + '+- %s' % self)
        if self.left_node:
            self.left_node.print_tree(indent=indent+1)
        if self.right_node:
            self.right_node.print_tree(indent=indent+1)

    def traverse(self):
        yield self
        if self.left_node:
            for node in self.left_node.traverse():
                yield node
        if self.right_node:
            for node in self.right_node.traverse():
                yield node

    def __iter__(self):
        return self.__next__()

    def __next__(self):
        yield self
        if self.left_node:
            yield from self.left_node
        if self.right_node:
            yield from self.right_node
        raise StopIteration

if __name__ == '__main__':
    my_tree = Node('Root',
        Node('L01',
            Node('L01L01'),
            Node('L01R01', 
                None, 
                Node('L01R01R01')
            ),
        ), 
        Node('R01',
            Node('R01L01'), 
            Node('R01R01')
        ), 
    )

    print('\n### print_tree results:')
    my_tree.print_tree()

    print('Basis for a search:')
    search_results = [str(i) for i in my_tree if i.data == 'L01R01R01']
    print(search_results)

    print('Basis for filtering:')
    filter_results = [str(i) for i in my_tree if 'R0' in i.data]
    print(filter_results)

    print('\n### __iter__ results:')
    for node in my_tree:
        print(node)

    print('\n### tree-data access by node-specification')
    root = Node('Root')
    L01 = Node('L01')
    root.left_node = L01
    L01L01 = Node('L01L01')
    L01.left_node = L01L01
    L01R01 = Node('L01R01')
    L01.left_node = L01R01

    # - Drilling into the tree to get to the Node with a 
    #   data-value of L01R01R01
    print(my_tree.left_node.right_node.right_node)

    # - Inserting a new value (or sub-tree) into a tree
    print(my_tree.right_node)
    my_tree.right_node = Node('new R01',
        None, 
        Node('new R01R01')
    )
    print(my_tree.right_node)
    print(my_tree.right_node.right_node)

# 'left':{'value':'L01', 'left':{}, 'right':{},},
# 'right':{'value':'R01', 'left':{}, 'right':{},},

example_as_dict = {
    'root':{
        'value':'root', 
        'left':{
            'value':'L01', 
            'left':{'value':'L01L01'},
            'right':{
                'value':'L01R01', 
                'right':{'value':'L01R01R01'},
            },
        },
        'right':{
            'value':'R01', 
            'left':{'value':'R01L01'},
            'right':{'value':'R01R01'},
        },
    }
}

import json
print(json.dumps(example_as_dict, indent=4).replace('"', "'"))
