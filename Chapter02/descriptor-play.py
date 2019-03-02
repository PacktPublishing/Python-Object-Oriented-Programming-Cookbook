class Descriptor:

    def init(self):
        self.__value = ''

    def __get__(self, instance, owner):
        print('Getting: %s' % self.__value)
        print('+- instance ... %s' % instance)
        print('+- owner ...... %s' % owner)
        return self.__value

    def __set__(self, instance, value):
        print('Setting: "%s"' % value)
        print('+- instance ... %s' % instance)
        print('+- value ...... %s' % value)
        self.__value = value.title()

    def __delete__(self, instance):
        print('Deleting: %s' % self.__value)
        print('+- instance ... %s' % instance)
        del self.__value

class Person:
    name = Descriptor()

    def __init__(self, name):
        self.name = name

if __name__ == "__main__":

    user = Person('name')
    print(user.name)
    user.name = 'john smith'
    print(user.name)
    del user.name

    import inspect
    print(inspect.isdatadescriptor(Descriptor))
