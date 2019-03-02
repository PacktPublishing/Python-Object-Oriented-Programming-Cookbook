#!/usr/bin/env python
"""
The complete code of Ch. 2, Recipe 1 -- Basic Class Definition
"""

class BasicClass:
    """Document the class as needed"""
    # Comments are allowed in classes
    # - Object initialization
    def __init__(self, name, description):
        """Object initialization"""
        # - Initialize instance properties from arguments
        self.name = name
        self.description = description
    # - Instance method
    def summarize(self):
        """Document method"""
        if self.description:
            return '%s: %s' % (self.name, self.description)
        else:
            return self.name

if __name__ == '__main__':
    print('#'*66)
    print('# BasicClass'.ljust(65, ' ') + '#')
    print('#'*66)
    print(BasicClass)
    # - Create an instance of the class
    instance = BasicClass('name', 'description')
    print('#- BasicClass instance '.ljust(65, '-') + '#')
    print(instance)
    print(instance.summarize())
