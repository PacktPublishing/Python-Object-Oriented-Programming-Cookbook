#!/usr/bin/env python
"""
The complete code of Ch. 2, Recipe 7 -- Creating class attributes
"""

class HasClassAttributes:
    """
A class that provides class attributes to play with
    """
    name = 'Name defined in class'
    number = 'one'

class InstanceAccess:
    # - Class attributes
    _active_instances = 0

    @property
    def active_instances(self):
        return self.__class__._active_instances

    @active_instances.setter
    def active_instances(self, value):
        self.__class__._active_instances = value

    def __init__(self):
        self.active_instances += 1

    def __del__(self):
        self.active_instances -= 1

if __name__ == '__main__':
    # - Print the class attributes
    print(HasClassAttributes.name)      # Name defined in class
    print(HasClassAttributes.number)    # one

    ### What happens if a class attribute is created and an 
    #   instance refers to it?
    # - Create an instance
    instance = HasClassAttributes()
    print(instance.name)                # Name defined in class
    print(instance.number)              # one

    ### What happens if an instance’s attribute-values are changed?
    # - Create an instance
    instance = HasClassAttributes()
    # - Alter the instance's values
    instance.name = 'New instance name'
    instance.number = 'two'
    # - Show the instance-values' changes
    print(instance.name)                # New instance name
    print(instance.number)              # two
    # - Show the class-attributes' values
    print(HasClassAttributes.name)      # Name defined in class
    print(HasClassAttributes.number)    # one

    ### What happens to an instance's values if the class values 
    #   are changed after the instance's values are changed?
    # - Create an instance
    instance = HasClassAttributes()
    instance.name = 'New instance name'
    instance.number = 'two'
    # - Alter the class' values
    HasClassAttributes.name = 'New class name'
    HasClassAttributes.number = 'three'
    # - Show the class-attributes' values
    print(HasClassAttributes.name)      # New class name
    print(HasClassAttributes.number)    # three
    # - Show the instance-values' changes
    print(instance.name)                # New instance name
    print(instance.number)              # two
    # - Create a NEW instance and show its values
    instance = HasClassAttributes()
    print(instance.name)                # New class name
    print(instance.number)              # three

    # - Reset the class to the original values
    HasClassAttributes.name = 'Name defined in class'
    HasClassAttributes.number = 'one'

    ### What happens to an instance's values if the class values 
    #   are changed after the instance has been created?
    # - Create an instance
    instance = HasClassAttributes()
    # - Alter the class' values
    HasClassAttributes.name = 'New class name'
    HasClassAttributes.number = 'three'
    # - Show the instance-values
    print(instance.name)                # New class name
    print(instance.number)              # three
    # - Reset the class to the original values
    HasClassAttributes.name = 'Name defined in class'
    HasClassAttributes.number = 'one'
    # - Create an instance
    instance = HasClassAttributes()
    # - Show ONE of the instance-values
    print(instance.name)                # Name defined in class
    # - Alter the class' values
    HasClassAttributes.name = 'New class name'
    HasClassAttributes.number = 'three'
    # - Show the OTHER of the instance-values
    print(instance.number)              # three

    inst1 = InstanceAccess()
    print('inst1.active_instances ... %d' % inst1.active_instances)
    inst2 = InstanceAccess()
    print('inst1.active_instances ... %d' % inst1.active_instances)
    print('inst2.active_instances ... %d' % inst2.active_instances)
    del inst1
    print('inst2.active_instances ... %d' % inst2.active_instances)
